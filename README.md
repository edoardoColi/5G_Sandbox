# 5G Sandbox

## Table of Contents
1. [Overview of 5G](#overview-of-5g)
2. [Overview of 802.11](#overview-of-80211)
3. [Comparison of 5G and 802.11](#comparison-of-5g-and-80211)
4. [Traffic MAC Analyzer (MACshuffle.sh)](#traffic-mac-analyzer-MACshufflesh)
	- [Execution](#execution)
	- [Security in WPA3](#security-in-wpa3)

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



i livelli nei pacchetti. a quale livello esiste il mac. cosa centra WPA3 con 802.11
cosa significa avere usa scheda di rete in monitor mode.
requisiti per l'uso e scopo del programma.



### Execution
To ensure seamless compatibility the program requires at least Bash v4.4.20, a popular and widely supported shell for Unix-like operating systems. Additionally, it utilizes TShark 3.6.7, a powerful command-line tool for capturing and analyzing network traffic based on the Wireshark engine.  
By leveraging the capabilities of Bash and TShark, the MAC Packet Analyzer script provides a user-friendly interface to facilitate counting random MACs against those encountered. We can run the program with the -h flag to get more detailed information.  
Below we find some execution references  

![Image description](https://github.com/edoardoColi/42_Roma_Luiss/blob/edoardoColi/42cursus/Born2beroot/Installer.png)


<img src=https://github.com/edoardoColi/42_Roma_Luiss/blob/edoardoColi/42cursus/Born2beroot/Installer.png width="60%" height="60%">


<img src=https://github.com/edoardoColi/5G_Sandbox/blob/edoardoColi/images/MACshuffle/NOME.png width="60%" height="60%">

### Security in WPA3
WPA3 is a security protocol for Wi-Fi networks introduced by the Wi-Fi Alliance. WPA3 is a security technology that is implemented on Wi-Fi networks based on the 802.11 standard.  
WPA3 (Wi-Fi Protected Access 3) was introduced to improve the security of Wi-Fi networks over the previous version of WPA2 security. Among the main reasons why WPA3 was introduced are:  
- Greater resistance to brute-force attacks:  
WPA3 uses a more robust authentication system than WPA2, based on the Dragonfly authentication algorithm. This makes it harder for attackers to crack down Wi-Fi network passwords.  
- Privacy improvements:  
WPA3 introduces a new forward secrecy encryption protocol that improves user privacy. This means that even if an attacker manages to decrypt the traffic of a Wi-Fi network session, they will not be able to decrypt the traffic of previous or subsequent sessions.  
- Security key management vulnerabilities:  
WPA3 improves security key management over WPA2 by introducing the Simultaneous Authentication of Equals (SAE) key exchange protocol. SAE provides greater protection against dictionary attacks and allows you to set stronger passwords.  
