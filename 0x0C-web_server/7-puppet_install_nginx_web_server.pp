class nginx {
  package { 'nginx':  # Install Nginx package
    ensure => installed,
  }

  service { 'nginx':  # Ensure Nginx service is running and enabled
    ensure => running,
    enable => true,
  }

  file { '/var/www/html/index.html':  # Create index.html file with "Hello World!" content
    ensure  => present,
    content => 'Hello World!',
    require => Package['nginx'],  # Require Nginx package to be installed
  }

  file { '/etc/nginx/sites-available/default':  # Configure Nginx server block
    ensure  => present,
    content => '
      server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;

        location = / {  # Handle root location
          return 200 "Hello World!";  # Return "Hello World!" with 200 status code
        }

        location = /redirect_me {  # Handle /redirect_me location
          return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;  # Perform 301 redirect
        }
      }
    ',
    require => Package['nginx'],  # Require Nginx package to be installed
    notify  => Service['nginx'],  # Notify Nginx service to restart if the configuration changes
  }
}

include nginx  # Include the nginx class in the manifest

