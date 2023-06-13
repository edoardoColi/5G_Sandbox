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

	with open(config_file, 'r') as file:
		for line in file:
			line = line.strip()
			if line.startswith('#'):		#Skip comment
				continue

			parts = line.split(" ")			#Parse the topology file using spaces
			if parts[0] == 'host':			#Parse hosts
				host_name = parts[1]
				host_ip = parts[2]
				host_nexthop = 'via ' + parts[3]
				topo.addHost(host_name, ip=host_ip, defaultRoute=host_nexthop)

			elif parts[0] == 'router':		#Parse routers
				router_name = parts[1]
				router_ip = parts[2]
				topo.addNode(router_name, cls=MyRouter, ip=router_ip)

			elif parts[0] == 'switch':		#Parse switches
				switch_name = parts[1]
				topo.addSwitch(switch_name)

			elif parts[0] == 'linkSH':		#Parse links switches to hosts
				node1 = parts[1]
				node2 = parts[2]
				topo.addLink(node1, node2)

			elif parts[0] == 'linkSS':		#Parse links switches to switches
				node1 = parts[1]
				node2 = parts[2]
				topo.addLink(node1, node2)

			elif parts[0] == 'linkHR':		#Parse links hosts to routers
				node1 = parts[1]
				node2 = parts[2]
				intf_name2 = parts[3]
				n2_ip = parts[4]
				topo.addLink(node1, node2, intfName2=intf_name2, params2={'ip' : n2_ip})

			elif parts[0] == 'linkRR':		#Parse links routers to routers
				node1 = parts[1]
				node2 = parts[2]
				intf_name1 = parts[3]
				intf_name2 = parts[4]
				ip1 = parts[5]
				ip2 = parts[6]
				topo.addLink(node1, node2, intfName1=intf_name1, intfName2=intf_name2, params1={'ip' : ip1}, params2={'ip' : ip2})
			
			# elif parts[0] == 'route':		#Parse routing tables
			# 	name = parts[1]
			# 	for node in topo.nodes():
			# 		if node == name:
			# 			(node).cmd('ip route add 0.0.0.0/0 via 10.0.0.1 dev r1-eth2')
			# 			break



			# (topo.getNodeByName('r1')).cmd('ip route add 0.0.0.0/0 via 10.0.0.1 dev r1-eth2')
	return topo

def run_topology(config_file):
	setLogLevel('info')		#Different logging levels are 'info' 'warning' 'error' 'debug'
	topo = build_topology(config_file)
	net = Mininet(topo=topo, link=TCLink)
	net.start()		#Starting the network

	with open(config_file, 'r') as file:		#Search in the configuration file for routing table
		for line in file:
			line = line.strip()
			if line.startswith('#'):		#Skip comment
				continue
			parts = line.split(" ")
			if parts[0] == 'route':		#Parse routing tables
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
	net.stop()		#Stopping the network

if __name__ == '__main__':
	run_topology('MininetTopo.conf')