from mininet.net import Mininet
from mininet.node import Controller
from mininet.log import setLogLevel
from mininet.cli import CLI
from pox.lib import of
import time
import matplotlib.pyplot as plt

# Create empty lists to store the timestamp and latency values
timestamps = []
latencies = []

class PacketCopyController(Controller):
    def __init__(self, name, target_host, **kwargs):
        Controller.__init__(self, name, **kwargs)
        self.target_host = target_host

    def _handle_PacketIn(self, event):
        packet = event.parsed
        self.packet_out(event.port, packet)
        self.packet_out_to_host(packet)
        # Measure latency and store timestamp and latency values
        latency = time.time() - event.created
        timestamps.append(time.time())
        latencies.append(latency)

    def packet_out(self, out_port, packet):
        msg = of.ofp_packet_out()
        msg.data = packet.pack()
        action = of.ofp_action_output(port=out_port)
        msg.actions.append(action)
        self.connection.send(msg)

    def packet_out_to_host(self, packet):
        host = self.net.get(self.target_host)
        if host:
            host.sendMsg(packet)

if __name__ == '__main__':
    setLogLevel('info')

    # Creazione della rete Mininet
    net = Mininet(controller=PacketCopyController)

    # Creazione degli host e degli switch
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    s1 = net.addSwitch('s1')

    # Creazione dei collegamenti
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    # Create the plot
    plt.figure()
    plt.xlabel('Time')
    plt.ylabel('Latency (seconds)')
    plt.title('Network Latency')

    # Avvio della rete e assegnazione del controller
        # Add the POX controller
    controller = net.addController(name='controller', target_host='h3', controller=PacketCopyController, ip='127.0.0.1', port=6633)
    net.start()
    controller.start()
    # controller = net.controllers[0]
    # controller.net = net

    # Start the plot animation
    plt.ion()
    plt.show()

    try:
        while True:
            # Update the plot with new latency data
            plt.plot(timestamps, latencies, 'b-')
            plt.draw()
            plt.pause(0.1)
    except KeyboardInterrupt:
        pass

    CLI(net)
    net.stop()
