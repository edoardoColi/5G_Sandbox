from mininet.net	import Mininet
from mininet.link	import TCLink
from mininet.topo	import Topo
from mininet.node	import Node
from mininet.cli	import CLI
from mininet.log	import setLogLevel
import subprocess
import multiprocessing

#
# for j in {1..20}; do echo "Test for runtest$j"; for i in {1..20}; do awk 'c&&!--c;/steffe'$i'/{c=7}' runtest$j|awk -F " " '{s+=$8}; END {printf "%d\n",s/100}' ;done; done
#

class MyRouter (Node):
	def config(self, **params):
		super(MyRouter, self).config(**params)
		self.cmd('sysctl net.ipv4.ip_forward=1')		#Enable forwarding on the router
	def terminate(self):
		self.cmd('sysctl net.ipv4.ip_forward=0')		#Disable forwarding on the router
		super(MyRouter, self).terminate

def run_command(host, command):
	# print("Sto per eseguire: "+command)
	output = host.cmd(command)
	# with open('runtestTraffic1', 'a') as file:##############################
	# 	file.write(output)
		# file.write(output + '************************************************************\n************************************************************\n')
	
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

			elif parts[0] == 'SN_link':		#Parse general links switches to nodes
				switch = parts[1]
				node = parts[2]
				bandwidth = int(parts[3])
				topo.addLink(elements.get(switch), elements.get(node), bw=bandwidth)

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
				switch = parts[1]
				router = parts[2]
				router_intfName = parts[3]
				router_intfIP = parts[4]
				topo.addLink(elements.get(switch), elements.get(router), intfName2=router_intfName, params2={'ip' : router_intfIP})

			elif parts[0] == 'linkSS':		#Parse links switches to switches
				switch1 = parts[1]
				switch2 = parts[2]
				topo.addLink(elements.get(switch1), elements.get(switch2))

			elif parts[0] == 'linkSH':		#Parse links switches to hosts
				switch = parts[1]
				host = parts[2]
				host_intfName = parts[3]
				topo.addLink(elements.get(switch), elements.get(host), intfName2=host_intfName)

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
			if parts[0] == 'route':			#Parse routing tables
				name = parts[1]
				pck_src = parts[2]
				pck_nexthop = parts[3]
				interf = parts[4]
				cmd = 'ip route add ' + pck_src + ' via ' + pck_nexthop + ' dev ' + interf
				(net.getNodeByName(name)).cmd(cmd)

	print("QUI PRIMA")

	(net.getNodeByName("steffe0")).cmd("iperf -s -P 2000 &")
	(net.getNodeByName("steffe1")).cmd("iperf -s -P 2000 &")
	(net.getNodeByName("steffe2")).cmd("iperf -s -P 2000 &")
	# (net.getNodeByName("steffe0")).cmd("rm -f esito.out")
	# (net.getNodeByName("steffe0")).cmd("iperf -P 100 -s > /dev/null &")##############################
	# hosts = ["steffe1","steffe2","steffe3","steffe4","steffe5","steffe6","steffe7","steffe8","steffe9","steffe10","steffe11","steffe12","steffe13","steffe14","steffe15","steffe16","steffe17","steffe18","steffe19","steffe20"]  # Esempio##############################

	# for i in range(0,100):
	# 	print(i)
	# 	processes = []
	# 	for host in hosts:
	# 		command = 'echo -n "Runned on "; date; echo '+host+'; iperf -c 10.0.0.1 -t 5'  # Esempio di comando (ping)
	# 		p = multiprocessing.Process(target=run_command, args=(net.getNodeByName(host), command))
	# 		p.start()
	# 		processes.append(p)

	# 	# Attende il completamento di tutti i processi
	# 	for p in processes:
	# 		p.join()
	print("QUI DOPO")

	CLI(net)
	net.stop()								#Stopping the network

if __name__ == '__main__':
		run_topology('SteffeCluster.conf')
