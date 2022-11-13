# Section 1 - Architect and deploy application

## 1.01 - Determine which configuration objects are necessary to optimally deploy an application

<details><summary>Determine least amount of configuration objects needed to deploy application</summary>  
</details>
<details><summary>Understand dependencies of configuration objects</summary>
</details>
<details><summary>Understand needed LTM profiles to deploy an application</summary>
</details>
<details><summary>Identify unnecessary configuration objects</summary>
</details>

## 1.02 - Determine whether or not an application can be deployed with only the LTM module provisioned

<details><summary>Identify the functionality of LTM configuration objects</summary>

* https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/ltm-concepts-11-5-1/3.html

</details>
<details><summary>Identify LTM profile settings to deploy an application</summary>

* https://support.f5.com/csp/article/K23843660  
</details>
<details><summary>Determine capabilities of LTM configuration objects</summary>
</details>

## 1.03 - Identify the difference between deployments (one arm, two arm, npath, Direct Server Return/DSR)

<details><summary>Identify configuration objects needed for L2/L3 npath routing</summary>

* L2 nPath:  
    - https://techdocs.f5.com/en-us/bigip-14-0-0/big-ip-local-traffic-manager-implementations-14-0-0/configuring-npath-routing.html
    - Default route on servers should point to the router instead of the BIG-IP
    - Servers should have the virtual server IP configured as loopback IPs
    - FastL4 profile with Loose Close setting
    - Same FastL4 profile with TCP Close Timeout setting same as the profile idle timeout
    - Server pool containing the backend servers
    - Virtual server with Performance (L4) type and previously created FastL4 profile
    - Same virtual server with Port and Address translation disabled

* L3 nPath:
    - https://support.f5.com/csp/article/K13403
    - Enable monitor encapsulation variable: *modify sys db tm.monitorencap value enable*
    - Server pool with encapsulation profile (IPIP or GRE), real server IPs
    - Transparent monitor monitoring the virtual server IP on the backend servers (loopback)
    - FastL4 profile with disabled hardware acceleration (PVA)
    - Virtual server with Translate Address disabled
    - Loopback IP on backend servers same as the Virtual Server IP
    - Encapsulation tunnel on backend servers 

</details>
<details><summary>Determine how the IP address changes when using DSR</summary>

* Initial traffic

| Source IP  | Destination IP |
| ------------- | ------------- |
| Client original IP  | Virtual Server IP  |
| Client original IP  | Backend server IP  |

* Reply traffic

| Source IP  | Destination IP |
| ------------- | ------------- |
| Backend server IP  | Client original IP  |

</details>
<details><summary>Determine how IP addresses change when using a fully proxy deployment</summary>

* Initial traffic

| Source IP  | Destination IP |
| ------------- | ------------- |
| Client original IP  | Virtual Server IP  |
| Automap or SNAT / SNAT Pool IP  | Backend server IP  |

* Reply traffic

| Source IP  | Destination IP |
| ------------- | ------------- |
| Backend server IP | Automap or SNAT / SNAT Pool IP  |
| Virtual Server IP  | Client original IP  |

</details>
<details><summary>Plan the network considerations for one arm and two arm deployments</summary>
</details>
<details><summary>Understand the importance of auto last-hop</summary>

* https://support.f5.com/csp/article/K13876
* Auto Last Hop is a setting that allows the BIG-IP system to track the source MAC address of incoming connections and return traffic from pools to the source MAC address, regardless of the routing table.
* When enabled, Auto Last Hop allows the BIG-IP system to send return traffic from pools to the MAC address that transmitted the request, even if the routing table points to a different network or interface. As a result, the BIG-IP system can send return traffic to clients even when there is no matching route. For example, if the BIG-IP system does not have a default route configured and the client is located on a remote network. 

|Object	|Scope	|Options	|Default setting	|Default setting definition|
| ------------- | ------------- | ------------- | ------------- | ------------- |
|Tunnel	|You can configure the setting on a per-Tunnel basis.	|Default, Enabled, Disabled	|Default	|The system uses Global Auto Last Hop.|
|VLAN group	|You can configure the setting on a per-VLAN group basis.	|Default, Enabled, Disabled	|Default	|The system uses Global Auto Last Hop.|
|VLAN	|You can configure the setting on a per-VLAN basis.	|Default, Enabled, Disabled	|Default	|The system uses Global Auto Last Hop.|
|SNAT	|You can configure the setting on a per-SNAT basis.	|Default, Enabled, Disabled	|Default	|The system uses Global Auto Last Hop.|
|NAT	|You can configure the setting on a per-NAT basis.	|Default, Enabled, Disabled	|Default	|The system uses Global Auto Last Hop.|
|Virtual server	|You can configure the setting on a per-server basis.	|Default, Enabled, Disabled	|Default	|The system uses Global Auto Last Hop.|

</details>

## 1.04 - Choose correct profiles and settings to fit application requirements

<details><summary>Identify LTM profile settings to deploy OneConnect</summary>
</details>
<details><summary>Determine which profiles are needed to deploy an application</summary>
</details>
<details><summary>Compare and contrast different communication protocols (TCP, UDP, FastL4)</summary>
</details>
<details><summary>Compare performance impacts of LTM profile settings</summary>
</details>

## 1.05 - Choose virtual server type and load balancing type to fit application requirements

<details><summary>Determine the difference between L2-L3 virtual servers</summary>
</details>
<details><summary>Compare and contrast standard and FastL4 virtual server types</summary>
</details>
<details><summary>Compare and contrast different load balancing methods</summary>
</details>
<details><summary>Identify different load balancing method use cases</summary>
</details>

## 1.06 - Determine how to architect and deploy multi-tier applications using LTM

<details><summary>Understand connection based architecture and when/how to apply</summary>
</details>
<details><summary>SNAT/Persistence/SSL settings in multi-tiered environment</summary>
</details>

## 1.07 - Distinguish between packet versus connection based load balancing

<details><summary>Demonstrate when to use packet based load balancing</summary>

* When only L3/L4 forwarding is needed, no need for any higher level inspection or decision making  
* https://ipwithease.com/packet-based-design-vs-full-proxy-design-in-f5/  
* Example: Performance Layer4 virtual server https://support.f5.com/csp/article/K8082  
</details>

<details><summary>Demonstrate when to use connection based load balancing</summary>

* Fully proxy loadbalancing, BIG-IP is acting as endpoint and originator of protocols 
* Example: Standard virtual server https://support.f5.com/csp/article/K8082 
* https://ipwithease.com/packet-based-design-vs-full-proxy-design-in-f5/  
* https://support.f5.com/csp/article/K55185917  

</details>

## 1.08 - Determine which configuration objects are necessary for applications that need the original client IP address

<details><summary>Determine when SNAT is required</summary>

* https://techdocs.f5.com/en-us/bigip-14-1-0/big-ip-tmos-routing-administration-14-1-0/nats-and-snats.html  
</details>

<details><summary>Determine the required SNAT type</summary>

* None, Automap, SNAT Pool, Intelligent SNAT (only within iRule)  
* https://support.f5.com/csp/article/K7820  
</details>

<details><summary>Identify functions of X-Forwarder-For</summary>

* https://support.f5.com/csp/article/K4816  
</details>

<details><summary>Outline the steps needed to return the traffic to LTM without SNAT</summary>

* Backend servers need to point to the BIG-IP as default gateway otherwise assymetric routing will happen and it can cause issues  
</details>

## 1.09 - Identify the matching order of multiple virtual servers

<details><summary>Identify which background server would process particular traffic</summary>

* https://support.f5.com/csp/article/K14800   
</details>

<details><summary>Identify why the virtual server fails to receive traffic</summary>
</details>

## 1.10 - Given a basic iRule's functionality, determine the profiles and configuration options necessary to implement the iRule

<details><summary>Determine what virtual server profile is necessary</summary>
</details>
<details><summary>Determine when persistence profile is necessary</summary>
</details>

## 1.11 - Describe how to deploy applications using iApp templates

<details><summary>Recognize how to modify an application depoyed with an iApp</summary>

* iApps -> Application Services -> Select the existing iApp -> Reconfigure tab

</details>
<details><summary>Identify objects created by an iApp</summary>

* iApps -> Application Services -> Select the existing iApp -> Components tab shows the objects created by the iApp
</details>
