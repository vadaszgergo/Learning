# Section 2 - Set up, administer and secure LTM devices

## 2.01 - Determine how to secure Self IPs

<details><summary>Identify which administrative services need to be accessible</summary>  
</details>
- Identify which configuration objects are allowing accessibility
- Identify which services must be enable for HA between devices

## 2.02 - Determine how to secure virtual servers

- Determine how to limit access to virtual servers
- Compare and contrast different virtual server types
- Identify LTM profile settings to limit access to virtual server resources

## 2.03 - Determine how to perform basic device configuration

- Identify how to sync time/date amongst LTM devices
- Determine how to limit administrative access to LTM devices (GUI/CLI)
- Identify how to restrict access to administrative partitions

## 2.04 - Determine how to perform a software upgrade while maintaining application availability

- Identify proper steps to avoid downtime while upgrading LTM softwre
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
- Demonstrate how to restrict access to management interface
- Demonstrate how to restrict access to virtual servers

## 2.07 - Determine how configuration changes affect existing and new connections

- Predict persistence for existing connections
- Calculate when changes will affect the connections
- Predict load balancing and persistence for new connections
- Determine the impact of virtual server configuration change on traffic

## 2.08 - Explain the uses of user roles, administrative partitions, and route domains

- Explain how to restrict access to LTM using user roles
- Discuss the benefits of administrative partitions
- Apply user roles to administrative partitions
- Explain the functionality of route domains
- Summarize how the 3 technologies can be used together

## 2.09 - Determine how to deploy or upgrade vCMP guests and how the resources are distributed

- Explain the different vCMP guest deployment states
- Discuss the relationship between CPU and memory on vCMP
- Select which versions can run a guest given host version
- Understand the relationship of network configuration objects between vCMP hosts and vCMP guests