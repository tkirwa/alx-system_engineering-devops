# Install and configure Nginx server with Puppet

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80;
      root /var/www/html;
      index index.html index.htm;
      
      location / {
        return 301 https://\$host\$request_uri;
      }
      
      location = /redirect_me {
        return 301 https://www.example.com/;
      }
    }
  ",
  notify  => Service['nginx'],
}

# Set index.html content
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
