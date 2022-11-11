# Section 2 - Set up, administer and secure LTM devices

## 2.01 - Determine how to secure Self IPs

<details><summary>Identify which administrative services need to be accessible</summary>  

- 

</details>

- Identify which configuration objects are allowing accessibility  

<details><summary>Identify which services must be enable for HA between devices</summary>  

- https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-device-service-clustering-admin-11-6-0/1.html
- Device Trust between boxes
- Device Group: Sync-Failover / Sync-Only
- Traffic Group: collection of objects that can float over to the other F5
- Config Sync IP address
- Failover IP address 
- Mirroring IP address
</details>

## 2.02 - Determine how to secure virtual servers

<details><summary>Determine how to limit access to virtual servers</summary>

- https://support.f5.com/csp/article/K42075438  
- Only allow specific source IP/range under the Virtual Server configuration page  
- Defined addresses in Shared Objects/Address List Section  
- Restring access using local traffic policies  
- Restrict access using iRules
- Restrict access using packet filters
</details>

<details><summary>Compare and contrast different virtual server types</summary>

- https://support.f5.com/csp/article/K55185917  
- Standard  
- Forwarding (Layer2)  
- Forwarding (IP)  
- Performance (Layer4)  
- Performance (HTTP)  
- Stateless  
- Reject  
- DHCP  
- Internal  
- Message Routing  
</details>

<details><summary>Identify LTM profile settings to limit access to virtual server resources</summary>

- https://support.f5.com/csp/article/K23843660  
- SSL profile: client authentication, disabling ciphers  
- Authentication profile: Radius, TACACS+, LDAP, SSL OCSP  
</details>

## 2.03 - Determine how to perform basic device configuration

<details><summary>Identify how to sync time/date amongst LTM devices</summary>

- Manual date/time setup: https://support.f5.com/csp/article/K3381 
- Configure NTP https://support.f5.com/csp/article/K13380  
- Checking and troubleshooting NTP https://support.f5.com/csp/article/K10240  

</details>

<details><summary>Determine how to limit administrative access to LTM devices (GUI/CLI)</summary>

- Limit access through User Roles
- Limit access to tmsh/shell/None for CLI
- https://techdocs.f5.com/en-us/bigip-14-0-0/big-ip-systems-user-account-administration-14-0-0/user-roles.html
</details>
<details><summary>Identify how to restrict access to administrative partitions</summary>

- System/Users --> Limit access to specific partition per user, or configure Remote Role Groups and restrict Group to specific partition  
- create auth user user2 { partition-access add { app1 { role application-editor } } password passwordhere }
</details>

## 2.04 - Determine how to perform a software upgrade while maintaining application availability

- Identify proper steps to avoid downtime while upgrading LTM software
- Determine necessary steps for migrating LTM configuration to new hardware
- Understand implications of stopping BIG-IP services

## 2.05 - Determine how to configure a high availability group of LTM devices to fit the requirements

- Compare and contrast traffic groups vs HA groups
- Determine what prevented an expected failover
- Describe the differences between network failover and hardware failover

## 2.06 - Apply concepts required to use BIG-IP functionality to fulfill security requirements

<details><summary>Make use of port lockdown</summary>  

https://support.f5.com/csp/article/K17333  
Control access level to each self IP. ICMP always allowed.  
Allow Default, Allow All, Allow None, Allow Custom  
When creating self IP, default lockdown is Allow None.  
Allow Default: tcp/udp 4353, tcp 443-22, tcp/udp 161 (SNMP), tcp/udp 53, udp 1026 (network failover)
</details>

<details><summary>Demonstrate how to restrict access to management interface</summary>

Multiple ways to achive this.
- HTTP access: modify /sys httpd allow add { <IP address or IP address range> }
- Network firewall rules (System/Platform/Security)
- SSH access - System/Platform/Configuration/SSH IP Allow
- SSH access - modify /sys sshd allow add {<ip_addr> or <ip_range> }
</details>

- Demonstrate how to restrict access to virtual servers

## 2.07 - Determine how configuration changes affect existing and new connections

- Predict persistence for existing connections  
- Calculate when changes will affect the connections  
- Predict load balancing and persistence for new connections  

<details><summary>Determine the impact of virtual server configuration change on traffic</summary>

- https://support.f5.com/csp/article/K13253  
- Changing the destination ip or port doesn't kill existing traffic  
- Changing the virtual server type kills existing traffic (Standard to Perf HTTP for example)
- Changing the HTTP profile doesn't kill existing traffic  
- Changing the TCP profile kills existing traffic
- Changing or removing client SSL profile kills existing traffic
- Adding or removing OneConnect setting kills existing traffic

</details>

## 2.08 - Explain the uses of user roles, administrative partitions, and route domains

<details><summary>Explain how to restrict access to LTM using user roles</summary>

https://techdocs.f5.com/en-us/bigip-14-0-0/big-ip-systems-user-account-administration-14-0-0/user-roles.html  

</details>

- Discuss the benefits of administrative partitions  
- Apply user roles to administrative partitions  
- Explain the functionality of route domains  
- Summarize how the 3 technologies can be used together  


## 2.09 - Determine how to deploy or upgrade vCMP guests and how the resources are distributed

<details><summary>Explain the different vCMP guest deployment states</summary>

https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/vcmp-administration-viprion-13-0-0/3.html  
- Configured: Initial and default state for a newly created guest. Not running, no resources allocated. If we change existing guest to this state from another, resources are deallocated, but virtual disks are not deleted.  
- Provisioned: Resources are allocated, if guest is new, then host allocates virtual disks and installs selected ISO image. A guest does not run while in Provisioned state. If changed from Deployed state, then it will be shutdown, but resources are going to stay as allocated.  
- Deployed: Host starts the guest and we can configure BIG-IP module within the guest.  
</details>

- Discuss the relationship between CPU and memory on vCMP
- Select which versions can run a guest given host version
- Understand the relationship of network configuration objects between vCMP hosts and vCMP guests
