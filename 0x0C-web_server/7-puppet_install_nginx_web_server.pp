# Puppet manifest to install and configure nginx

# Install nginx package
package { 'nginx':
  ensure => installed,
}

# Add a line to the nginx configuration file for redirection
file_line { 'Redirect /redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# Create the index.html file with 'Hello World!' content
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Start and enable the nginx service
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
