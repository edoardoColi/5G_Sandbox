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
	elements = {}  # Dictionary to store nodes

	# h1 = topo.addHost('H1', ip='161.46.247.2/25', defaultRoute='via 161.46.247.1')
	# h2 = topo.addHost('H2', ip='161.46.247.3/25', defaultRoute='via 161.46.247.1')

	s1 = topo.addSwitch('S1')

	# h4 = topo.addHost('H4', ip='161.46.247.131/26', defaultRoute='via 161.46.247.129')
	# h3 = topo.addHost('H3', ip='161.46.247.196/27', defaultRoute='via 161.46.247.195')

	r1 = topo.addNode('R1', cls=MyRouter, ip='161.46.247.1/25')
	r2 = topo.addNode('R2', cls=MyRouter, ip='161.46.247.253/30')

	### Ordine importante ###
	topo.addLink(r1, s1, intfName1='R11', params1={'ip' : '161.46.247.1/25'})
	
	topo.addLink(r2, r1, intfName2='R13', intfName1='R21', params2={'ip' : '161.46.247.254/30'}, params1={'ip' : '161.46.247.253/30'})

	# topo.addLink(r2, h3, intfName2='H31', intfName1='R22', params1={'ip' : '161.46.247.195/27'})
	# topo.addLink(r2, h4, intfName2='H41', intfName1='R23', params1={'ip' : '161.46.247.129/26'})


	# topo.addLink(s1, h1, intfName2='H11')
	# topo.addLink(s1, h2 ,intfName2='H21')
	
	return topo

def run_topology(config_file):
	setLogLevel('info')		#Different logging levels are 'info' 'warning' 'error' 'debug'
	topo = build_topology(config_file)
	net = Mininet(topo=topo, link=TCLink)
	net.start()		#Starting the network

	# (net.getNodeByName('R1')).cmd('ip route add 161.46.247.192/27 via 161.46.247.254 dev R13')
	# (net.getNodeByName('R1')).cmd('ip route add 161.46.247.128/26 via 161.46.247.254 dev R13')

	if net.pingAll():
		print(Fore.RED + "Network has issues" + Style.RESET_ALL)
	else:
		print(Fore.GREEN + "Network working properly" + Style.RESET_ALL)
	CLI(net)
	net.stop()		#Stopping the network

if __name__ == '__main__':
	run_topology('MininetTopo.conf')