### Two Secured and Monitored Web Infrastructure
![](https://raw.githubusercontent.com/tkirwa/alx-system_engineering-devops/master/0x09-web_infrastructure_design/images/2-secured_and_monitored_web_infrastructure.jpg)

#### [Visit the Board](https://miro.com/app/board/uXjVMEXJwTc=/ "Visit the Board")

**Explanation:**

*   **Firewalls:** Firewalls are added to protect the infrastructure from unauthorized access and potential attacks. They act as a barrier between the external network and the servers, monitoring and filtering network traffic based on predetermined security rules.
    
*   **Load Balancer (with SSL Termination):** The load balancer acts as a central entry point for incoming traffic, distributing it across multiple web servers. It also terminates SSL (Secure Sockets Layer) connections, allowing encrypted HTTPS traffic to be decrypted and forwarded to the web servers.
    
*   **Web Server (Nginx):** The web server handles incoming HTTP requests, serving static content, and forwarding dynamic requests to the application server.
    
*   **Application Server:** The application server hosts the application files and processes dynamic requests. It interacts with the web server to generate responses based on the requested actions.
    
*   **Database (MySQL):** The database server stores and manages the website's data, handling read and write operations. It is responsible for data persistence and retrieval.
    
*   **SSL Certificate (HTTPS):** An SSL certificate is added to serve the website over HTTPS. HTTPS ensures encrypted communication between the server and the client, providing security and protecting sensitive data from interception.
    
*   **Monitoring Clients (Data Collectors):** Monitoring clients collect data from various components of the infrastructure, including servers, load balancers, and databases. They send this data to a monitoring service (e.g., Sumologic) for analysis and reporting.
    

**Monitoring Clients (Data Collectors):** Monitoring clients collect data from various components of the infrastructure, including servers, load balancers, and databases. They send this data to a monitoring service (e.g., Sumologic) for analysis and reporting.

**Specifics about the Infrastructure:**

*   **Firewalls:** Firewalls are crucial for securing the infrastructure by controlling incoming and outgoing network traffic, filtering based on security policies, and preventing unauthorized access.
    
*   **HTTPS Traffic:** Serving traffic over HTTPS ensures encryption between the server and the client, securing data transmission and protecting against eavesdropping and tampering.
    
*   **Monitoring:** Monitoring is used to track the health, performance, and availability of the infrastructure. It helps detect issues