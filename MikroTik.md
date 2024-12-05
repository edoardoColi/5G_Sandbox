# Create VLANs
go to Interfaces > Interface List. Add VLAN interfaces and assign each interface to your LAN bridge, and specify the VLAN ID.
```
/interface vlan
add interface=bridge1 name=vlan10 vlan-id=10
add interface=bridge1 name=vlan20 vlan-id=20
add interface=bridge1 name=vlan30 vlan-id=30
...
```
# Assign Ports to VLANs
Go to Bridge > VLANs. For each VLAN ID, assign the corresponding group.
```
/interface bridge vlan
add bridge=bridge1 tagged=bridge1 untagged=ether1,ether4 vlan-ids=10
add bridge=bridge1 tagged=bridge1 untagged=ether7,ether8 vlan-ids=20
add bridge=bridge1 tagged=bridge1 untagged=ether9 vlan-ids=30
...
```
# Configure Bridge VLAN Filtering
Enable VLAN filtering for the bridge. Remember that this can cut you off the network if not properly setup.
```
/interface bridge set bridge1 vlan-filtering=yes
```
# Set up DHCP Servers
Create Address Pools. Go to IP > Pool.
```
/ip pool
add name=pool10 ranges=192.168.10.2-192.168.10.254
add name=pool20 ranges=192.168.20.2-192.168.20.254
add name=pool30 ranges=192.168.30.2-192.168.30.254
...
```
Set Up DHCP Networks. Go to IP > DHCP Server > Networks.
```
/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.1
add address=192.168.20.0/24 gateway=192.168.20.1
add address=192.168.30.0/24 gateway=192.168.30.1
...
```
Go to IP > DHCP Server and add a DHCP server for each VLAN, using the corresponding pool.
```
/ip dhcp-server
add address-pool=pool10 disabled=no interface=vlan10 name=dhcp10
add address-pool=pool20 disabled=no interface=vlan20 name=dhcp20
add address-pool=pool30 disabled=no interface=vlan30 name=dhcp30
...
```
# Set PVID
The PVID assigns a VLAN ID to untagged incoming traffic. Without setting the PVID, untagged traffic will remain unclassified or assigned to the default VLAN (usually VLAN 1), which can lead to miscommunication and connectivity issues.
```
/interface bridge port print

/interface bridge port set [find interface=ether1] pvid=10
/interface bridge port set [find interface=ether2] pvid=20
/interface bridge port set [find interface=ether3] pvid=30
...
```
# Firewall
When you enable `/interface bridge settings set use-ip-firewall=yes`, it means that IP-level firewall rules in the /ip firewall section will now apply to traffic passing through the bridge.
Performance Considerations: Enabling use-ip-firewall=yes adds CPU overhead since the bridge traffic is now inspected by the firewall. On high-performance CRS switches, offloading VLAN handling to hardware (Layer 2 switch chip) is more efficient than relying on the CPU for firewall rules.
If use-ip-firewall=yes is Disabled use /interface bridge vlan and Layer 2 filtering for VLAN isolation as:
```
/interface bridge vlan
add bridge=bridge1 vlan-ids=10 untagged=ether1,ether2
add bridge=bridge1 vlan-ids=20 untagged=ether3,ether4
...
```
### Chains
In MikroTik RouterOS, a chain in firewall rules refers to a predefined or user-defined set of rules within the firewall that processes traffic based on its type and direction. Chains are used to organize and structure firewall rules for easier management and efficiency.
Predefined Chains in MikroTik:
- Input: This chain is responsible for filtering traffic that is destined for the router itself.
- Output: This chain filters traffic that originates from the router itself.
- Forward: This chain filters traffic that is being routed through the router.
Custom Chains can be defined to organize and reuse firewall rules more effectively.
## USE CASE
```
/interface vlan
add interface=bridge1 name=vlan100 vlan-id=100

/ip address
add address=192.168.100.1/24 interface=vlan100

;;; Allow Management VLAN Traffic
/ip firewall filter
add chain=input action=accept in-interface=vlan100

;;; Allow Essential Services
/ip firewall filter
add chain=input action=accept protocol=udp dst-port=67-68 in-interface=bridge1 comment="Allow DHCP"
add chain=input action=accept protocol=udp dst-port=53 in-interface=bridge1 comment="Allow DNS"

;;; Drop All Other Traffic to Management Services
/ip firewall filter
add chain=input action=drop in-interface=!vlan100
```
Enabling use-ip-firewall=yes under /interface bridge settings is not required to restrict management access to only VLAN X.
The use-ip-firewall=yes setting allows the Layer 2 (bridge) traffic to be processed by the IP firewall rules. This is typically used for advanced filtering of bridge-level traffic but can impact performance because all bridge traffic is sent to the CPU for processing.
In this case, you are controlling management access using the input chain of the IP firewall, which applies to traffic destined to the MikroTik itself (Layer 3). This is independent of Layer 2 (bridge) filtering.

# Security
For Additional Security you can
```
;;; Restrict by Source IP
/ip firewall filter
add chain=input action=accept src-address=192.168.100.10 in-interface=vlan100
add chain=input action=drop in-interface=!vlan100

;;; Disable Unused Services or change default ports
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www-ssl disabled=yes

set ssh port=2202
set www port=8080
```
# Saving configuration
Key Differences Between Backup and Export
| **Feature**            | **Binary Backup**        | **Export Configuration** |
|-------------------------|--------------------------|---------------------------|
| **Format**             | Binary                  | Human-readable script    |
| **Portability**        | Specific to the device  | Can be edited and reused |
| **Includes Passwords** | Yes                    | No                       |

```
;;; will save in system fs a .backup file
/system backup save name=my_backup
;;; will save in system fs a .rsc file
/export file=my_config

;;; system will automatically reboot after this command
/system backup load name=my_backup.backup
;;; execute the commands in the file to recreate the configuration
/import file=my_config.rsc
```
# Updating MikroTik RouterOS
Best Practices:
- Backup Before Updating: Always create a binary backup and export configuration before updates.
- Check Compatibility: Review changelogs for potential issues or breaking changes.
- Test on Non-Critical Devices: Test updates on non-production routers before applying to critical systems.
```
;;; Check for Updates
/system package update check-for-updates

;;; Download and Install Updates
/system package update download
/system package update install

;;; Verify the Update after rebooting
/system resource print

;;; Update RouterBOARD Firmware
/system routerboard upgrade
/system reboot

```
