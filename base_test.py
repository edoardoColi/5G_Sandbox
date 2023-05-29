import configparser
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

# def build_topology(config_file):
# 	topo = Topo()

# 	# Create a host with the desired interface and IP
# 	hh = topo.addHost('h1', ip='161.46.247.196/24', defaultRoute='via 161.45.247.195')
# 	hh.setDefaultRoute = ''
# 	topo.addHost('h2', ip='161.46.247.197/24', defaultRoute='via 161.45.247.195')

# 	# Create a router with an interface and default route
# 	topo.addNode('r1', cls=MyRouter, ip='161.46.247.195/24')

# 	# Add a link between the host and router
# 	topo.addLink('h1', 'r1')
# 	topo.addLink('h2', 'r1')
# 	return topo

class MyTopo (Topo):

	def build( self, *args, **params ):
		host = self.addHost('h1', ip='161.46.247.196/24')
		host.setDefaultRoute('via 161.45.247.195')
		self.addHost('h2')
		self.addNode('r1', cls=MyRouter)

		self.addLink('h1', 'h2')
		# self.addLink('h1', 'r1', intfName1='H11', intfName2='R11', params1={'ip' : '161.46.247.131/26'}, params2={'ip' : '161.46.247.129/26'})
		# self.addLink('h2', 'r1', intfName1='H21', intfName2='R12', params1={'ip' : '161.46.247.196/27'}, params2={'ip' : '161.46.247.195/27'})


def run_topology(config_file):
	setLogLevel('info')		#Different logging levels are 'info' 'warning' 'error' 'debug'
	net = Mininet(link=TCLink)

	# Create a host with the desired interface and IP
	host = net.addHost('h1', ip='161.46.247.196/24')

	# Set the default route on the host
	host.setDefaultRoute('via 161.45.247.195')

	# Create a router with two interfaces and default routes
	router = net.addHost('router', cls=MyRouter)

	# Add interfaces to the router
	net.addLink(router, host, intfName1='r33', intfName2='h31', params1={'ip': '161.46.247.195/24'}, params2={'ip': '161.46.247.196/24'})
	# net.addLink(router, intfName1='r21', params1={'ip': '161.46.247.129/30'})

	# Set the default routes on the router
	router.cmd('ip route add default via 161.46.247.254 dev r33')
	router.cmd('ip route add default via 161.46.247.130 dev r21')


	net.start()		#Starting the network
	# (net.getNodeByName('h1')).cmd('ip route add 0.0.0.0/0 via 161.46.247.129')
	# (net.getNodeByName('h2')).cmd('ip route add 0.0.0.0/0 via 161.46.247.195')
	# (net.getNodeByName('r1')).cmd('ip route add 0.0.0.0/0 via 161.46.247.254')

	net.pingAll()
	CLI(net)
	net.stop()		#Stopping the network

if __name__ == '__main__':
	run_topology('MininetTopo.conf')