# Adjusts the file limit for the Nginx process.

# Replace the existing ULIMIT value in the nginx configuration file
exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

# Restart the Nginx service to apply the changes
exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
