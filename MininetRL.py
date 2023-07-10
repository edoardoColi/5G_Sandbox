import mininet
import time, socket, random
import numpy as np
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink
import matplotlib.pyplot as plt

# Define custom topology
class MyTopology(Topo):
    def build(self):
        # Create switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        
        # Create hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        
        # Add links
        self.addLink(h1, s1, cls=TCLink, delay='10ms', bw=1)
        self.addLink(s1, s2, cls=TCLink, delay='50ms', bw=0.5)
        self.addLink(s2, h2, cls=TCLink, delay='10ms', bw=1)

# Define TCP agent
class MyTCPAgent:
    def __init__(self):
        # Initialize TCP agent
        self.transmission_rounds = []
        self.congestion_window_sizes = []

    
    def handle_connection(self):
        print("TCP connection establishment")
        # Implement TCP connection establishment

        # Example TCP connection establishment using a socket
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.connect(('localhost', 19191))

        # Example TCP connection establishment simulation
        time.sleep(1)  # Simulating connection establishment delay

    def handle_data_transfer(self, tunnel, window_size):
        print("Performing data transfer with tunnel:", tunnel, "and window size:", window_size)
        # Implement TCP data transfer with the given tunnel and window size using socket programming
        
        # Implement TCP data transfer simulation
        
        # Placeholder logic: Simulating data transfer
        # time.sleep(0.1)  # Simulating data transfer delay
        
        # Simulate congestion control by waiting for a fixed amount of time
        time.sleep(0.1)

        # Record transmission round and final congestion window size
        self.transmission_rounds.append(len(self.transmission_rounds) + 1)
        self.congestion_window_sizes.append(window_size)

# Define RL agent for tunnel selection
class TunnelSelectionAgent:
    def __init__(self, tunnels):
        # Initialize your RL agent for tunnel selection
        self.rewards = []
        self.selected_tunnels = []
        self.tunnels = tunnels
        self.current_tunnel = 0
    
    def select_tunnel(self):
        # Implement tunnel selection based on RL policy
        # Placeholder logic: Select a tunnel randomly or based on some criteria
        selected_tunnel = self.tunnels[self.current_tunnel]
        self.current_tunnel = (self.current_tunnel + 1) % len(self.tunnels)
        return selected_tunnel
    
    def update_policy(self, reward):
        # Implement RL policy update based on rewards
        self.rewards.append(reward)
        self.selected_tunnels.append(self.select_tunnel())

# Define RL agent for window prediction
class WindowPredictionAgent:
    def __init__(self):
        # Initialize the RL agent for window prediction
        self.window_sizes = [1, 2, 4, 8, 16, 32, 64]  # Possible window sizes
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.q_table = {}  # Q-table to store state-action values
    
    def predict_window_size(self):
        # Get the current state (e.g., network conditions)
        state = self.get_state()

        # Check if the state is in the Q-table
        if state not in self.q_table:
            # Initialize Q-values for all possible actions in the current state
            self.q_table[state] = {window_size: 0 for window_size in self.window_sizes}

        # Choose the action (window size) based on epsilon-greedy policy
        if random.random() < 0.2:  # Exploration (20% of the time)
            action = random.choice(self.window_sizes)
        else:  # Exploitation (80% of the time)
            action = self.get_best_action(state)

        return action

    def get_state(self):
        # Implement the logic to determine the current state based on network conditions
        # For example, you can consider factors such as round-trip time, packet loss rate, or congestion signals

        # Placeholder logic: Return a random state
        return random.randint(1, 10)

    def get_best_action(self, state):
        # Find the action (window size) with the highest Q-value for the given state
        best_action = max(self.q_table[state], key=self.q_table[state].get)
        return best_action 
       
    def update_policy(self, reward):
        # Update the Q-value based on the reward received after taking an action
        # Get the previous state and action
        prev_state = self.get_state()  # Replace with the actual previous state
        prev_action = self.predict_window_size()  # Replace with the actual previous action

        # Get the current state
        curr_state = self.get_state()

        # Check if the current state is in the Q-table
        if curr_state not in self.q_table:
            # Initialize Q-values for all possible actions in the current state
            self.q_table[curr_state] = {window_size: 0 for window_size in self.window_sizes}

        # Update the Q-value using the Q-learning update rule
        max_q_value = max(self.q_table[curr_state].values())  # Get the maximum Q-value for the current state
        self.q_table[prev_state][prev_action] += self.alpha * (reward + self.gamma * max_q_value - self.q_table[prev_state][prev_action])

# Main function
if __name__ == '__main__':
    setLogLevel('info')
    
    # Create the Mininet network
    topo = MyTopology()
    net = Mininet(topo=topo)
    net.start
    
    # Instantiate TCP and RL agents
    tcp_agent = MyTCPAgent()
    tunnels = ['myPrivate1']
    tunnel_agent = TunnelSelectionAgent(tunnels)
    window_agent = WindowPredictionAgent()
    
    # Perform TCP connection establishment
    tcp_agent.handle_connection()
    
    # Perform data transfer with RL-based tunnel selection and window prediction
    start_time = time.time()
    while True:
        if time.time() - start_time > 10:  # End packet exchange after <X> seconds
            break
        tunnel = tunnel_agent.select_tunnel()
        window_size = window_agent.predict_window_size()

        # Perform data transfer
        tcp_agent.handle_data_transfer(tunnel, window_size)

        # Update RL agents based on rewards
        reward = -0.5  # Actual reward value
        tunnel_agent.update_policy(reward)
        # window_agent.update_policy(reward)

    # Stop the Mininet network
    net.stop()

    # Plot Transmission Round and Congestion Window Size
    plt.plot(tcp_agent.transmission_rounds, tcp_agent.congestion_window_sizes)
    plt.xlabel('Transmission Round')
    plt.ylabel('Congestion Window Size')
    plt.title('TCP+RL Window Prediction')
    plt.show()
