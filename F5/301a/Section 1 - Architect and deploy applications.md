# Section 1 - Architect and deploy application

## 1.01 - Determine which configuration objects are necessary to optimally deploy an application

- Determine least amount of configuration objects needed to deploy application  
- Understand dependencies of configuration objects
- Understand needed LTM profiles to deploy an application
- Identify unnecessary configuration objects

## 1.02 - Determine whether or not an application can be deployed with only the LTM module provisioned

- Identify the functionality of LTM configuration objects
- Identify LTM profile settings to deploy an application
- Determine capabilities of LTM configuration objects

## 1.03 - Identify the difference between deployments (one arm, two arm, npath, Direct Server Return/DSR)

- Identify configuration objects needed for L2/L3 npath routing
- Determine how the IP address changes when using DSR
- Determine how IP addresses change when using a fully proxy deployment
- Plan the network considerations for one arm and two arm deployments
- Understand the importance of auto last-hop

## 1.04 - Choose correct profiles and settings to fit application requirements

- Identify LTM profile settings to deploy OneConnect
- Determine which profiles are needed to deploy an application
- Compare and contrast different communication protocols (TCP, UDP, FastL4)
- Compare performance impacts of LTM profile settings

## 1.05 - Choose virtual server type and load balancing type to fit application requirements

- Determine the difference between L2-L3 virtual servers
- Compare and contrast standard and FastL4 virtual server types
- Compare and contrast different load balancing methods
- Identify different load balancing method use cases

## 1.06 - Determine how to architect and deploy multi-tier applications using LTM

- Understand connection based architecture and when/how to apply
- SNAT/Persistence/SSL settings in multi-tiered environment

## 1.07 - Distinguish between packet versus connection based load balancing

<details><summary>Demonstrate when to use packet based load balancing</summary>
    <p>

    ```ruby
    When only L3/L4 forwarding is needed, no need for any higher level inspection or decision making  
    https://ipwithease.com/packet-based-design-vs-full-proxy-design-in-f5/  
    Example: Performance Layer4 virtual server https://support.f5.com/csp/article/K8082  
    ```
    
    </p>
    </details>

- Demonstrate when to use connection based load balancing
    - Fully proxy loadbalancing, BIG-IP is acting as endpoint and originator of protocols  
    https://ipwithease.com/packet-based-design-vs-full-proxy-design-in-f5/  
    https://support.f5.com/csp/article/K55185917  
    https://support.f5.com/csp/article/K8082  

## 1.08 - Determine which configuration objects are necessary for applications that need the original client IP address

- Determine when SNAT is required
    - https://techdocs.f5.com/en-us/bigip-14-1-0/big-ip-tmos-routing-administration-14-1-0/nats-and-snats.html  

- Determine the required SNAT type
    - None, Automap, SNAT Pool, Intelligent SNAT (ony within iRule)
    - https://support.f5.com/csp/article/K7820  

- Identify functions of X-Forwarder-For
    - https://support.f5.com/csp/article/K4816  

- Outline the steps needed to return the traffic to LTM without SNAT
    - Backend servers need to point to the BIG-IP as default gateway otherwise assymetric routing will happen and it can cause issues

## 1.09 - Identify the matching order of multiple virtual servers

- Identify which bg server would process particular traffic
    - https://support.f5.com/csp/article/K14800   
- Identify why the virtual server fails to receive traffic

## 1.10 - Given a basic iRule's functionality, determine the profiles and configuration options necessary to implement the iRule

- Determine what virtual server profile is necessary
- Determine when persistence profile is necessary

## 1.11 - Describe how to deploy applications using iApp templates

- Recognize how to modify an application depoyed with an iApp
- Identify objects created by an iApp
