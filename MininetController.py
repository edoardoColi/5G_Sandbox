from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

class CustomController( Controller ):
    "Open vSwitch controller"
    def __init__( self, name, **kwargs ):
        kwargs.setdefault( 'command', self.isAvailable() or
                           'ovs-controller' )
        Controller.__init__( self, name, **kwargs )


# class CustomController(Controller):
#     def _handle_ConnectionUp(self, event):
#         # Handle new connection
#         dpid_str = dpid_to_str(event.dpid)
#         log.info("Switch %s connected", dpid_str)
#         self.connection = event.connection
#         event.connection.addListeners(self)

#     def _handle_PacketIn(self, event):
#         # Handle incoming packet
#         packet = event.parsed
#         if packet.type == ethernet.IP_TYPE:
#             ip_packet = packet.payload
#             src_ip = ip_packet.srcip
#             dst_ip = ip_packet.dstip
#             log.info("Source IP: %s, Destination IP: %s", src_ip, dst_ip)

#         # Call the parent handler to continue processing other events
#         super(CustomController, self)._handle_PacketIn(event)

def create_topology():
    net = Mininet(controller=Controller, switch=OVSSwitch)

    # Create network nodes
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1', cls=OVSSwitch)

    # Create links
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start the network
    net.start()

    # Create a custom controller instance
    controller = net.addController('c1', controller=CustomController)

    # Connect the switch to the controller
    s1.start([controller])

    # Enter command line mode
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()
