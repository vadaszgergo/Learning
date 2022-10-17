# Section 1 - Architect and deploy application

## 1.01 - Determine which configuration objects are necessary to optimally deploy an application

- Determine least amount of configuration objects needed to deploy application  
- Understand dependencies of configuration objects
- Understand needed LTM profiles to deploy an application
- Identify unnecessary configuration objects

## 1.02 - Determine whether or not an application can be deployed with only the LTM module provisioned

<details><summary>Identify the functionality of LTM configuration objects</summary>
</details>
<details><summary>Identify LTM profile settings to deploy an application</summary>
</details>
<details><summary>Determine capabilities of LTM configuration objects</summary>
</details>

## 1.03 - Identify the difference between deployments (one arm, two arm, npath, Direct Server Return/DSR)

<details><summary>Identify configuration objects needed for L2/L3 npath routing</summary>
</details>
<details><summary>Determine how the IP address changes when using DSR</summary>
</details>
<details><summary>Determine how IP addresses change when using a fully proxy deployment</summary>
</details>
<details><summary>Plan the network considerations for one arm and two arm deployments</summary>
</details>
<details><summary>Understand the importance of auto last-hop</summary>
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

* None, Automap, SNAT Pool, Intelligent SNAT (ony within iRule)  
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
</details>
<details><summary>Identify objects created by an iApp</summary>
</details>
