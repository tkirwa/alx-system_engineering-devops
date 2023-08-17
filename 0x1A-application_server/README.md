## 0x1A. Application server
### DevOps | SysAdmin
## Getting PIDs of Process using Port

Here's a simpler and more direct way to get the PIDs of processes using ports 5000 and 5001:

1. To get the PID using port 5000:

   ```bash
   sudo lsof -t -i :5000
   ```

2. To get the PID using port 5001:

   ```bash
   sudo lsof -t -i :5001
   ```

Replace the port numbers with the actual ports you want to check. Running these commands should give you the PIDs of the processes using the specified ports. Once you have the PIDs, you can use the `kill` command to terminate the processes:

```bash
sudo kill PID
```
Replace `PID` with the actual PID you obtained from the previous commands.

## Force Terminate a Process

It seems that the process with PID 3146045 is not terminating as expected. This can sometimes happen if a process is stuck or unresponsive. Let's try a more forceful approach to terminate the process:

1. To forcefully terminate a process, you can use the `kill` command with the `-9` option, which sends the `SIGKILL` signal to the process. This signal is more aggressive and should terminate the process even if it's unresponsive.

   ```bash
   sudo kill -9 3146045
   ```

2. After sending the `SIGKILL` signal, you can check again if the process is still running using:

   ```bash
   sudo lsof -t -i :5000
   ```

If the process is still not terminating after using the `-9` option, it might indicate a more complex issue. You could try to investigate the process further or consider restarting your system if that's feasible.

Please be cautious when using the `kill -9` command, as it forcefully terminates the process without allowing it to perform cleanup operations. This might lead to potential data loss or corruption if used without careful consideration.

------------


## Set up Production Environment with Gunicorn
To set up your production environment with Gunicorn, you'll need to follow these steps on your `web-01` server:

1. **Install Gunicorn:**

   First, make sure you're in your project directory. Then, install Gunicorn using `pip3`, which is the Python package manager:

   ```bash
   pip3 install gunicorn
   ```

2. **Create a Gunicorn Configuration File (Optional):**

   You can create a Gunicorn configuration file if you want to customize Gunicorn's behavior. For example, create a `gunicorn_config.py` file with the following content:

   ```python
   bind = "0.0.0.0:5000"
   workers = 2
   ```

   This configuration specifies that Gunicorn should bind to all available network interfaces on port 5000 and use 2 worker processes. You can adjust the configuration according to your needs.

3. **Start Gunicorn:**

   Start Gunicorn by specifying your Flask application object as the entry point. Assuming your Flask app is located in a file named `0-hello_route.py` and the application object is named `app`, you can use the following command:

   ```bash
   gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
   ```

   If you created a Gunicorn configuration file, you can specify it using the `--config` option:

   ```bash
   gunicorn --config gunicorn_config.py web_flask.0-hello_route:app
   ```

   This will start Gunicorn with your Flask app on port 5000, binding to all available network interfaces.

4. **Verify Gunicorn Setup:**

   You can use `curl` to test if your Gunicorn setup is working correctly. Open a new terminal and run:

   ```bash
   curl 127.0.0.1:5000/airbnb-onepage/
   ```

   You should see the output from your Flask app, similar to "Hello HBNB!" as in the example.

   **Note:** The example mentions that the checker will bind a Gunicorn instance to port 6000 for testing, so make sure nothing is listening on that port.

This setup will allow you to run your Flask app using Gunicorn in a production environment on port 5000.
------------


## Serve Flask app through Nginx
To serve your Flask app through Nginx, you need to configure Nginx as a reverse proxy. Here's how you can do it:

1. **Create Nginx Configuration:**

   Create a new Nginx configuration file named `2-app_server-nginx_config` (or any other suitable name) in the appropriate Nginx configuration directory (usually `/etc/nginx/sites-available/`). Open the file in a text editor:

   ```bash
   sudo nano /etc/nginx/sites-available/2-app_server-nginx_config
   ```

   Add the following configuration to the file:

   ```nginx
   server {
       listen 80;
       server_name _;

       location /airbnb-onepage/ {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   }
   ```

   Save the file and exit the text editor.

2. **Create a Symbolic Link:**

   Create a symbolic link from the configuration file in the `sites-available` directory to the `sites-enabled` directory to enable the configuration:

   ```bash
   sudo ln -s /etc/nginx/sites-available/2-app_server-nginx_config /etc/nginx/sites-enabled/
   ```

3. **Test Nginx Configuration:**

   Before restarting Nginx, it's a good idea to check if your configuration is correct:

   ```bash
   sudo nginx -t
   ```

   If the configuration test is successful, proceed to the next step.

4. **Restart Nginx:**

   Restart Nginx to apply the new configuration:

   ```bash
   sudo service nginx restart
   ```

5. **Start Your Gunicorn Application:**

   Make sure your Gunicorn application is running on port 5000. You can run it using the command you used before:

   ```bash
   gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app
   ```

6. **Testing:**

   You can now test the setup by accessing your application through the Nginx server. Use `curl` or your web browser to access the following URL:

   ```
   http://your_server_ip/airbnb-onepage/
   ```

   You should see the output from your Flask app, similar to "Hello HBNB!".

Please replace `your_server_ip` with the actual IP address or domain name of your server.

This setup will configure Nginx to proxy requests to your Gunicorn application on port 5000, allowing you to serve your Flask app through Nginx on port 80.