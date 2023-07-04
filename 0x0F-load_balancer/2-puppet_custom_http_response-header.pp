# custom http header response NGiNX

# Update package repositories
exec {'update':
  command => '/usr/bin/apt-get update',
}

# Ensure NGINX package is present
-> package {'nginx':
  ensure => 'present',
}

# Add a custom line to the nginx.conf file
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',  # Specify the line to match in the file
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",  # Add a new line with the custom header
}

# Start the NGINX service
-> exec {'run2':
  command => '/usr/sbin/service nginx start',
}
