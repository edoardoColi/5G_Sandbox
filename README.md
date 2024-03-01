# Communication Sandbox

## Table of Contents
1. [Overview of 5G](#overview-of-5g)
2. [Overview of 802.11](#overview-of-80211)
3. [Comparison of 5G and 802.11](#comparison-of-5g-and-80211)
4. [Traffic MAC Analyzer (MACshuffle.sh)](#traffic-mac-analyzer-MACshufflesh)
    - [Execution](#execution)
    - [Security in WPA3](#security-in-wpa3)
5. [Mininet](#mininet)
    - [Automating Network with the Mininet Python API](#automating-network-with-the-mininet-python-api)
    - [Building Custom Network Topologies (MininetNetPractice.py)](#building-custom-network-topologies-mininetnetpracticepy)
6. [5G Network simulation](#5g-network-simulation)
    - [Vagrant commands](#vagrant-commands)
    - [Example overview](#example-overview)
    - [Example execution](#example-execution)
7. [Why sandbox?](#why-sandbox)
## Overview of 5G
5G is the fifth generation of wireless technology that promises to deliver faster data transfer speeds, lower latency, and increased network capacity. It is designed to enable a wide range of new applications and use cases that were previously not possible with 4G technology. 5G technology is based on a new radio access technology which uses higher frequency bands (millimeter waves) than previous generations of wireless technology. This allows 5G networks to deliver much faster data transfer speed. In addition offer greater network capacity, which means they can support more devices for the growth of the Internet of Things (IoT) and also promises to reduce latency to under 1 millisecond, which is critical for real-time applications such as gaming, remote surgery, autonomous machines.  
Overall, 5G is expected to revolutionize the way we use wireless technology and enable new applications that were previously not possible. However, the rollout of 5G networks is still ongoing and faces challenges such as the need for more infrastructure and the use of higher frequency bands that have limited coverage compared to lower frequency bands.  

## Overview of 802.11
802.11 is a set of standards for wireless local area networks (WLANs) developed by the Institute of Electrical and Electronics Engineers (IEEE). It is commonly known as Wi-Fi, and it allows devices to connect to the internet or other devices wirelessly. The 802.11 standards define the protocols and technologies for wireless communication, including the frequency bands used for transmission, the data transfer rates, the security and encryption methods used to protect the data being transmitted. There are several different versions of the 802.11 standard, including 802.11a, 802.11b, 802.11g, 802.11n, and 802.11ac, each with different specifications and capabilities. Wi-Fi has become an essential part of modern networking, enabling wireless connectivity in homes, offices, and public spaces.  
There are also other 802 standards that define specifications for wired local area networks (e.g. 802.3 Ethernet), personal area wireless networks (e.g. 802.15 Bluetooth), and metropolitan area wireless networks (e.g. 802.16 WiMAX).  

## Comparison of 5G and 802.11
5G and 802.11 are both wireless communication technologies, but they differ in several key areas. Here's a comparison of 5G and Wi-Fi in terms of their similarities and differences, use cases and applications, advantages and disadvantages.  
- Similarities and differences:  
Both 5G and 802.11 are wireless communication technologies that use radio waves to transmit data. However, they differ in their frequency bands, coverage areas, and data rates. 5G operates in higher frequency bands, providing faster data speeds but requiring more infrastructure to provide coverage. 802.11 operates in lower frequency bands and is primarily used for local area networking.
- Use cases and applications:  
5G is primarily used for mobile communications, including smartphones, IoT devices, and autonomous vehicles. It can also be used for industrial automation, virtual and augmented reality, and other applications that require high-speed, low-latency data transfer. Wi-Fi is primarily used for local area networking, such as in homes, offices, and public spaces. It can also be used for IoT applications and other low-bandwidth use cases.
- Advantages and disadvantages:  
5G offers faster data transfer rates, lower latency, and greater capacity than Wi-Fi. However, it requires more infrastructure and is more expensive to deploy. Wi-Fi is more widely available and less expensive to deploy, but it has lower data transfer rates and higher latency.

5G and 802.11 will continue to coexist and there would be the possibility for convergence between the two technologies.  

## Traffic MAC Analyzer (MACshuffle.sh)
Network layers, play a crucial role in the design and operation of computer networks. These layers provide a structured approach to network communication by dividing the complex process into manageable tasks. Each layer has a specific set of functions and protocols that contribute to the overall operation of the network. From the physical layer responsible for transmitting bits over the physical medium to the application layer that interacts directly with user applications, each layer builds upon the services provided by the layer below it. This hierarchical arrangement allows for modular design, interoperability, and easier troubleshooting. The concept of protocol layers, as defined by models like OSI and TCP/IP, serves as a foundation for efficient and reliable network communication in today's interconnected world.  
  
The MAC (Media Access Control) is a sublayer of the second layer called the "Data Link Layer" in the OSI reference model and the TCP/IP model. MAC is responsible for managing MAC addresses, which are unique identifiers associated with each device's network interface. MAC addresses are used to correctly route data packets to the correct recipient within a local area network.  
  
Support for randomized MAC addresses is not always available on all Android devices due to hardware or software limitations. In some cases, older devices may not be able to support randomized MAC address functionality. In addition, the implementation of randomized MAC addresses may also be affected by the privacy and security policies of the device manufacturer or mobile network operator. Some manufacturers may decide not to implement this feature because it is not part of their security and privacy goals, or because their security policy is to use static MAC addresses for traceability and device identification reasons.  
  
In order to capture packets at the MAC (Media Access Control) layer, it is necessary to have "Wi-Fi adapter in promiscuous mode" aka "Wi-Fi sniffer". This is because Wi-Fi networks use a wireless medium where multiple devices share the same frequency band for communication. In the normal operation mode Wi-Fi adapter only captures and processes packets that are specifically addressed to it. However, when a Wi-Fi component is set to monitor mode, it can capture all packets transmitted within its range, regardless of their destination MAC address. It allows the Wi-Fi network administrators to gain insights into network performance, identify potential security vulnerabilities, detect unauthorized devices or activities, and optimize network configurations.  
### Execution
To ensure seamless compatibility the program requires at least Bash v4.4.20, a popular and widely supported shell for Unix-like operating systems. Additionally, it utilizes TShark 3.6.7, a powerful command-line tool for capturing and analyzing network traffic based on the Wireshark engine.  
By leveraging the capabilities of Bash and TShark, the MAC Packet Analyzer script provides a user-friendly interface to facilitate counting random MACs against those encountered. We can run the program with the -h flag to get more detailed information.  
```
./MACshuffle.sh -h
```
Below we find some execution references:  
<img src=https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/images/MACshuffle/analyze_file.png width="105%" height="105%">  
*Expected output for analyzing a capture file passed to the program in differents ways.*  
<br>
<br>
<img src=https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/images/MACshuffle/unicity_bounded_test.png width="105%" height="105%">  
*Expected output for performing the same analysis as before but with combination of unicity flag and n flag to bound the number of packets analyzed.*  
<br>
<br>
<img src=https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/images/MACshuffle/versose_test.png width="105%" height="105%">  
*Expected output for running the analysis using the verbose flag. More details are shown regarding the counts.*  
<br>
<br>
<img src=https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/images/MACshuffle/verbose_unicity_test.png width="105%" height="105%">  
*Expected output for running the same analysis but accounting for duplicates.*  
  
To perform a stream data analysis in a certain interface we can use the following command (in this case it's necessary to have tcpdump).
```
sudo tcpdump -i <interface> -U -w .MACprobe.tmp | ./MACshuffle.sh -p
```

### Security in WPA3
WPA3 is a security protocol for Wi-Fi networks introduced by the Wi-Fi Alliance. WPA3 is a security technology that is implemented on Wi-Fi networks based on the 802.11i standard.  
WPA3 (Wi-Fi Protected Access 3) was introduced to improve the security of Wi-Fi networks over the previous version of WPA2 security. Among the main reasons why WPA3 was introduced are:  
- Greater resistance to offline brute-force(dictionary) attacks:  
WPA3 uses a more robust authentication system than WPA2, based on the Dragonfly authentication algorithm. This makes it harder for attackers to crack down Wi-Fi network passwords.  
- Privacy improvements:  
WPA3 introduces a new forward secrecy (FS) encryption protocol that improves user privacy. This means that even if an attacker manages to decrypt the traffic of a Wi-Fi network session, they will not be able to decrypt the traffic of previous or subsequent sessions.  
- Security key management vulnerabilities:  
WPA3 improves security key management over WPA2 by introducing the Simultaneous Authentication of Equals (SAE) key exchange protocol. SAE provides greater protection against dictionary attacks and allows you to set stronger passwords.  

## Mininet
Mininet is an open-source network emulator that allows users to create virtual networks on a single machine. It provides a realistic environment for testing and developing networking software without the need for expensive physical hardware. By leveraging Linux's network namespaces and lightweight virtualization techniques, Mininet can emulate a complete network topology.  
Emulation, as exemplified by Mininet, aims to replicate the behavior of real systems by executing the actual software stack. It creates a faithful representation of a network by running real operating systems. Emulation preserves the intricacies and complexities of the system being emulated, enabling accurate performance analysis and software testing.  
Simulation, on the other hand, involves creating a model of a system and observing its behavior under different conditions. It typically abstracts away certain details to focus on specific aspects of the system. In network simulation, models are built to analyze network protocols, traffic patterns, or the effects of various configurations.  
### Automating Network with the Mininet Python API 
The Mininet API for Python are a powerful tool that allows users to interact with and control Mininet virtual networks programmatically. API provides a comprehensive set of classes and methods that enable fine-grained control over network topologies and network elements such as hosts, switches, and links. Users can create custom network topologies by defining the desired number of hosts, switches, and their interconnections. They can also specify parameters such as link capacities, delays, and loss rates to emulate real-world network conditions accurately.  
In addition to its network emulation capabilities, Mininet also provides support for various controllers, allowing users to simulate the behavior of network control planes. It offers a range of controller options, including popular ones like OpenFlow-based controllers such as Ryu, POX, and Floodlight. These controllers enables the development and testing of SDN (Software-Defined Networking) applications and algorithms in a controlled environment.  
### Building Custom Network Topologies (MininetNetPractice.py)
In order to build a custom network topology I used Mininet  and Python tools; in front of all to run the program we need to install those dependencies:
```
sudo -v
sudo apt install python3 python3-pip openvswitch-testcontroller mininet;
pip3 install --upgrade pip;
pip3 install mininet colorama configparser ryu pillow pox matplotlib;
```
The *MininetNetPractice.py* program showcases the ability to parse and extract data from the configuration file to define the desired network topology. Using the Mininet API, the program reads and parses the *MininetTopo.conf* file, which contains information about the network topology. By leveraging the parsed data, the program creates a virtual network with the desired topology, replicating the specified network configuration. This allows for the creation of custom and complex network scenarios tailored to specific research or testing requirements.  
Referring to a random topology, like the one in the figure below, we can create a configuration file that brings back exactly these parameters within the Mininet topology in order to interact with them. The configuration file *MininetTopo.conf* represents it. Some notes for the creation are reported there as a structure model, together with some constraints to be respected. Another important aspect to allow the network to function is to manage the routers routing table(**TODO inside MininetTopo.conf**).
<img src=https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/images/MininetConf/topology.jpeg width="105%" height="105%">  
I tested the mininet emulation software to reproduce a real situation of a cluster. Within this [file.pdf](https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/docs/MininetConf/researchReport.pdf) it is possible to view all my comparison analysis and the conclusions I have reached.  

## 5G Network simulation
For emulating and testing a 5G Network we are going to use ComNetsEmu, a testbed and network emulator designed for the NFV/SDN teaching book "Computing in Communication Networks: From Theory to Practice".  
We are taking all the installing information from official [website](https://git.comnets.net/public-repo/comnetsemu), if needed there is also a dumped comnetsemu public-repo webpage in [this pdf](https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/docs/Dump_public-repo_comnetsemu.pdf). The recommended and easiest way to install ComNetsEmu is to use Vagrant and Virtualbox; for this reason I provided a *setupVirtualBox.sh* script to automate the installation.  
Long story short commands are:
```
$ cd ~
$ git clone https://git.comnets.net/public-repo/comnetsemu.git
$ cd ./comnetsemu
$ vagrant up comnetsemu
  #Take a break and wait about 15 minutes

  #SSH into the VM when it's up and ready (The ComNetsEmu banner is printed on the screen)
$ vagrant ssh comnetsemu
```
Once in the Virtual Machine upgrade source code of ComNetsEmu Python package with:
```
$ cd ~/comnetsemu
$ git checkout master
$ git pull origin master

$ cd ~/comnetsemu/util
$ bash ./install.sh -u
  #Rerun if the result is unsatisfactory

$ cd ~/comnetsemu/
$ sudo make test && sudo make test-examples
```
**Warning**: Main developers of ComNetsEmu does not use Windows
and does not have a Windows machine to test on.  
If you are using Windows, they recommend using [MobaXterm](https://mobaxterm.mobatek.net/)
as the console. This should solve problems opening `xterm` in the emulator.  
```
Session <-- To create a new session in MobaXterm  
    SSH > Remote host: 127.0.0.1
        > Specify username: vagrant
        > port: 2222
        Advanced SSH settings > Enable X11-Forwarding
                            > Remote environment: Interactive shell
        > password: vagrant
```
Windows Subsystem Linux(wsl) is a valid option for running Ubuntu on Windows([setup link](https://youtu.be/X-DHaQLrBi8?feature=shared)).
### Vagrant commands
Vagrant uses "base boxes" to bring up your local machines. These are several Vagrant commands which you can use to control your box.  
Some of the important ones are:  
- **vagrant up** : Bring a box online.  
- **vagrant status** : Show current box status.  
- **vagrant suspend** : Pause the current box.  
- **vagrant resume** : Resume the current box.  
- **vagrant halt** : Shutdown the current box.  
- **vagrant destroy** : Destroy the current box. By running this command, you will lose any data stored on the box.  
- **vagrant snapshot** : Take a snapshot of the current box.  

[Pointer to more details...](https://opensource.com/article/21/9/test-vagrant)
### Example Overview
The 5G architecture is designed to be more flexible, scalableand adaptable to the needs of various applications and services. Here we have the key components of the 5G architecture.  

<img src=https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/images/5G_architecture.jpg width=1000px></img>

**Acronymes list:**
- *User Equipement* UE
- *Control Plane* CP
- *User Plane* UP
- *evolved NodeB* eNB
- *User Plane Function* UPF
- *Access and Mobility Function* AMF
- *Session Management Function* SMF
- *Policy Control Function* PCF
- *Radio Access Network* RAN
- *Evolved Packet System* EPS
- *Evolved Packet Core* EPC

There are many open-source implementation of 5G both for RAN and Core.  
For the Radio Access Network we are going to use [UERANSIM](https://github.com/aligungr/UERANSIM).  
For the 5G Core Network we are going to use [OPEN5gs](https://github.com/open5gs).  
In the context of alternatives [OpenAirInterface](https://github.com/openairinterface) presents itself as another viable option, both for [RAN](https://openairinterface.org/oai-5g-ran-project/) and [Core](https://openairinterface.org/oai-5g-core-network-project/).  
The testing scenario includes 5 DockerHosts as shown in the figure below. The UE starts two PDU session one for each slice defined in the core network.  

<img src=https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/images/5G_topology.jpg width=1000px></img>

<!-- Observe the Round Trip Time using uesimtun0 (slice 1 - reaching the UPF in the "cloud DC" with DNN="internet" ) and ueransim1 (slice 2 - reaching the UPF in the 'mec DC' with DNN="mec")

nella simulazione andiamo ad usare 'Open5gs' implementation Per 5G Core implementation.
nella simulazione usiamo 'UERANSIM' implementation Per RAN implementation

Immagine della topologia della simulazione...
(5G we have one phisical network and we want network sliceing, on same infrastructure. We want to try this in the simulation)
Virtual host "upf_emc" -> "user-plane functionalities_multi-edge cloud" (simula near the edge, poca latenza)
Virtual host "upf" (simula il cloud, molta latenza)
Virtual host "cp" -> "Control plane" (con anche altre funzionalita della reta)
AMF=Access Mobility Function?
SMF=S... Mobility Function?
    //{22:50} intervento del prof.

    //{40:20} intervento del prof.
poi immagini delle implementazioni per GNB e UE

Le slices che abbiamo fatto sono quelle verdi, una per Edge e una per Cloud
Immagine della network implementation in generale con switch e cose
altre immagini di configurazioni
    //{1:10:20} intervento del prof.

ifconfig -- dovremmo essere capaci di vedere i due tunnel uesimtun0 e uesimtun1 -->

### Example Execution
The previous overview is based on the 5G deployment in comnetsemu of [Riccardo Fedrizzi](https://github.com/RiccardoFedrizzi). We con start cloning his project and building it
```
$ cd ~/comnetsemu/app
$ git clone https://github.com/RiccardoFedrizzi/comnetsemu_5Gnet.git
$ cd ~/comnetsemu/app/comnetsemu_5Gnet/build
$ ./build.sh
```
or alternatively download docker images from DockerHub, so instead of *build.sh* use
```
$ ./dockerhub_pull.sh
```
Execution **dependencies** (Python packages: `sudo pip3 install pymongo`) must be installed befor running the examples.  
In the directory we will find [*example1.py*](https://github.com/RiccardoFedrizzi/comnetsemu_5Gnet/blob/main/example1.py) and [*example2.py*](https://github.com/RiccardoFedrizzi/comnetsemu_5Gnet/blob/main/example2.py)
- the first one is about using webUI to add UE, and we [refer to this](https://github.com/RiccardoFedrizzi/comnetsemu_5Gnet?tab=readme-ov-file#running-example1py).
- the second creates the same environment of *example1.py* but the open5GS control plane configuration is done programmatically without using the webUI, we [refer to this](https://github.com/RiccardoFedrizzi/comnetsemu_5Gnet?tab=readme-ov-file#running-example2py).  

**! ! !** To enter the containers must be executed `sudo python3 example2.py` and in another terminal `sudo ./enter_container.sh ue`**! ! !**  
## Why sandbox?

Using Docker, or a Virtual Machine, as a sandbox offers a powerful solution for isolating and testing applications and services in a controlled environment. Docker containers provide a lightweight, reproducible way to create sandboxes for development, testing, or experimentation. By encapsulating an application and its dependencies within a container, developers can ensure consistency across different environments, making it easier to troubleshoot issues and prevent conflicts. Docker's sandboxing capabilities also enhance security by isolating processes and resources, reducing the risk of unintended interactions or vulnerabilities. Whether for development, QA, or exploring new software, Docker's sandboxing approach simplifies the management of isolated environments, fostering agility and reliability in software development workflows.
```
docker run -it --rm ubuntu /bin/sh
docker system prune --all --volumes --force #Remove unused data 
   # --all     remove all unused images
   # --volumes prune anonymous volumes
   # --force   does not prompt for confirmation
```
