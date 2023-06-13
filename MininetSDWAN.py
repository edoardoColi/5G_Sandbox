import heapq
import random
from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.link import TCLink
from mininet.net	import Mininet
from mininet.topo	import Topo
from mininet.node	import Node
from mininet.cli	import CLI
from mininet.link	import TCLink
from mininet.log	import setLogLevel

class MyRouter (Node):
    def config(self, **params):
        super(MyRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')		#Enable forwarding on the router
    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')		#Disable forwarding on the router
        super(MyRouter, self).terminate

def create_topology():
    net = Topo()

    # Create the SD-WAN sites
    site1 = net.addHost('site1')
    site2 = net.addHost('site2')
    site3 = net.addHost('site3')

    # Create the virtual SD-WAN devices
    sdwan1 = net.addHost('sdwan1')
    sdwan2 = net.addHost('sdwan2')

    # Create switches
    switch1 = net.addSwitch('s1')

    # Connect the hosts and switches
    net.addLink(site1, switch1, bw=10, delay='10ms')
    net.addLink(site2, switch1, bw=5, delay='20ms')
    net.addLink(site3, switch1, bw=8, delay='15ms')
    net.addLink(sdwan1, switch1, bw=100, delay='1ms')
    net.addLink(sdwan2, switch1, bw=100, delay='1ms')

    return net

def dynamic_path_selection(net, link_qos):    # Function to select the best path based on real-time conditions using Dijkstra algorithm with QoS metrics

    # Add a random factor to the QoS metric
    random_range = 4
    for link in link_qos:
        link_qos[link] += random.randint(-random_range, random_range)

    # Perform Dijkstra algorithm to find the best path based on QoS metrics
    def dijkstra(source):
        distance = {node: float('inf') for node in net}
        distance[source] = 0
        queue = [(0, source)]
        while queue:
            dist, node = heapq.heappop(queue)
            if dist > distance[node]:
                continue
            for neighbor, _, link_info in net[node].connectionsTo(net):
                qos = link_qos.get(link_info[0].intf1.name)
                new_dist = dist + qos
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))
        return distance

    # Run Dijkstra algorithm from each site to determine the best path
    site1_distance = dijkstra('site1')
    site2_distance = dijkstra('site2')
    site3_distance = dijkstra('site3')
    sdwan1_distance = dijkstra('sdwan1')
    sdwan2_distance = dijkstra('sdwan2')

    # Select the best path based on minimum total QoS distance
    best_path = min(site1_distance, site2_distance, site3_distance, sdwan1_distance, sdwan2_distance,
                    key=lambda x: sum(x.values()))
    print("Best path based on QoS metrics:")
    for node, distance in best_path.items():
        print(f"Node: {node}, Total QoS Distance: {distance}")
        
def run_topology():
    setLogLevel('info')		#Different logging levels are 'info' 'warning' 'error' 'debug'
    topo = create_topology()
    net = Mininet(topo=topo, link=TCLink)
    # net.addController('c0', controller=Controller) #non serve metterlo esplicitamente

    net.start()		#Starting the network
    # Define QoS metrics for each link (example values)
    link_qos = {
        'site1-eth0': 8,   # QoS value for link site1 -> switch1
        'site2-eth0': 6,   # QoS value for link site2 -> switch1
        'site3-eth0': 9,   # QoS value for link site3 -> switch1
        'sdwan1-eth0': 10, # QoS value for link sdwan1 -> switch1
        'sdwan2-eth0': 7   # QoS value for link sdwan2 -> switch1
    }

    # Add a random factor to the QoS metric
    random_range = 4
    for link in link_qos:
        link_qos[link] += random.randint(-random_range, random_range)

    dynamic_path_selection(net, link_qos)
    CLI(net)
    net.stop()		#Stopping the network

if __name__ == '__main__':
    run_topology()