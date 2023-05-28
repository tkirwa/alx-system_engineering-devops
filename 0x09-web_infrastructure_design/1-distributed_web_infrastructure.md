### 0ne-Server Web Infrastructure
![](https://raw.githubusercontent.com/tkirwa/alx-system_engineering-devops/master/0x09-web_infrastructure_design/images/1-distributed_web_infrastructure.jpg)

#### [Visit the Board](https://miro.com/app/board/uXjVMEXwjm8=/ "Visit the Board")
**Explanation:**

*   **Server 1 (Nginx):** This server acts as a web server, serving static content and handling incoming HTTP requests from clients. It is responsible for receiving and routing the requests.
    
*   **Load Balancer (HAproxy):** The load balancer distributes incoming requests across multiple application servers to achieve load balancing and high availability. It improves performance and ensures that no single server is overloaded. The specific distribution algorithm used by the load balancer could be round-robin, least connections, or other algorithms. The algorithm determines how the load balancer selects the next server to handle each incoming request.
    
*   **Server 2 (Application):** This server hosts the application files and executes the code base specific to the website. It receives requests from the load balancer, processes them, and generates dynamic content to send back as responses.
    
*   **Database (MySQL):** The database server stores and manages the website's data. It handles read and write operations, allowing the application server to retrieve and store information.
    

*   The load balancer enables a load distribution mechanism, such as a round-robin algorithm. This algorithm distributes incoming requests evenly among the available application servers, ensuring each server receives a fair share of the traffic.
    
*   The load balancer enables an Active-Passive setup. In this setup, the load balancer directs all the traffic to the active (primary) application server. If the active server fails, the load balancer automatically switches to the passive (backup) server to ensure continuous service availability.
    
*   In a Primary-Replica (Master-Slave) cluster, the Primary node (database server) is the main server responsible for handling write operations (inserting, updating, and deleting data) from the application. The Replica nodes (also known as Slave nodes) replicate the data from the Primary node and handle read operations, offloading the read traffic from the Primary node.
    
*   The issues with this infrastructure are as follows:
    
    *   **Single Point of Failure (SPOF):** The load balancer itself becomes a single point of failure. If the load balancer fails, the entire infrastructure can be affected. Additionally, if either the web server or the application server fails, the website's availability and performance can be impacted.
        
    *   **Security Issues:** This infrastructure lacks essential security measures such as a firewall and HTTPS. Without a firewall, the system is vulnerable to unauthorized access and potential attacks. The absence of HTTPS can compromise data security and privacy.
        
    *   **No Monitoring:** The absence of monitoring tools and processes makes it challenging to identify and address performance issues, resource utilization, and potential failures in the infrastructure. Monitoring is crucial for maintaining the health and availability of the system.