import configparser
from colorama		import Fore, Style
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

def build_topology(config_file):
	topo = Topo()
	elements = {}  							# Dictionary to store nodes

	with open(config_file, 'r') as file:
		for line in file:
			line = line.strip()
			if line.startswith('#'):		#Skip comment
				continue
			parts = line.split(" ")			#Parse the topology file using spaces
			if parts[0] == 'N_host':			#Parse hosts
				host_name = parts[1]
				elements[host_name] = topo.addHost(host_name)

			elif parts[0] == 'N_router':		#Parse routers
				router_name = parts[1]
				elements[router_name] = topo.addNode(router_name)

			elif parts[0] == 'N_switch':		#Parse switches
				switch_name = parts[1]
				elements[switch_name] = topo.addSwitch(switch_name)

			elif parts[0] == 'NN_link':		#Parse general links nodes to nodes
				node1 = parts[1]
				node2 = parts[2]
				topo.addLink(elements.get(node1), elements.get(node2))

			if parts[0] == 'host':			#Parse hosts
				host_name = parts[1]
				host_ip = parts[2]
				host_nexthop = 'via ' + parts[3]
				elements[host_name] = topo.addHost(host_name, ip=host_ip, defaultRoute=host_nexthop)

			elif parts[0] == 'router':		#Parse routers
				router_name = parts[1]
				router_ip = parts[2]
				elements[router_name] = topo.addNode(router_name, cls=MyRouter, ip=router_ip)

			elif parts[0] == 'linkRR':		#Parse links routers to routers
				router1 = parts[1]
				router1_intfName = parts[2]
				router1_intfIP = parts[3]
				router2 = parts[4]
				router2_intfName = parts[5]
				router2_intfIP = parts[6]
				topo.addLink(elements.get(router1), elements.get(router2), intfName1=router1_intfName, intfName2=router2_intfName, params1={'ip' : router1_intfIP}, params2={'ip' : router2_intfIP})

			elif parts[0] == 'linkRH':		#Parse links routers to hosts
				host = parts[1]
				host_intfName = parts[2]
				router = parts[3]
				router_intfName = parts[4]
				router_intfIP = parts[5]
				topo.addLink(elements.get(host), elements.get(router), intfName1=host_intfName, intfName2=router_intfName, params2={'ip' : router_intfIP})

			elif parts[0] == 'linkRS':		#Parse links routers to switches
				node1 = parts[1]
				node2 = parts[2]
				# topo.addLink	TODO

			elif parts[0] == 'linkSS':		#Parse links switches to switches
				node1 = parts[1]
				node2 = parts[2]
				# topo.addLink	TODO

			elif parts[0] == 'linkSH':		#Parse links switches to hosts
				node1 = parts[1]
				node2 = parts[2]
				# topo.addLink	TODO

	return topo

def run_topology(config_file):
	setLogLevel('info')						#Different logging levels are 'info' 'warning' 'error' 'debug'
	topo = build_topology(config_file)
	net = Mininet(topo=topo, link=TCLink)
	net.start()								#Starting the network
	with open(config_file, 'r') as file:	#Search in the configuration file for routing table
		for line in file:
			line = line.strip()
			if line.startswith('#'):		#Skip comment
				continue
			parts = line.split(" ")
			if parts[0] == 'N_route':			#Parse routing tables
				name = parts[1]
				pck_src = parts[2]
				pck_nexthop = parts[3]
				# cmd = 'ip route add ' + pck_src + ' via ' + pck_nexthop TODO
				# (net.getNodeByName(name)).cmd(cmd)
			elif parts[0] == 'route':			#Parse routing tables
				name = parts[1]
				pck_src = parts[2]
				pck_nexthop = parts[3]
				interf = parts[4]
				cmd = 'ip route add ' + pck_src + ' via ' + pck_nexthop + ' dev ' + interf
				(net.getNodeByName(name)).cmd(cmd)
	if net.pingAll():
		print(Fore.RED + "Network has issues" + Style.RESET_ALL)
	else:
		print(Fore.GREEN + "Network working properly" + Style.RESET_ALL)
	CLI(net)
	net.stop()								#Stopping the network

if __name__ == '__main__':
	run_topology('MininetTopo.conf')