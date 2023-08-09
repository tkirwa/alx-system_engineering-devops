# Define a file resource to manage the content of wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure  => present, # Ensure the file exists
  content => file('/var/www/html/wp-settings.php').content.gsub('phpp', 'php'), # Replace 'phpp' with 'php' in the file content
  notify  => Exec['restart_apache'], # Notify the restart_apache exec resource if changes are made
}

# Define an exec resource to restart the Apache service
exec { 'restart_apache':
  command => 'systemctl restart apache2', # Command to restart the Apache service
  path    => '/usr/local/bin/:/bin/', # Set the PATH for the command execution
  refreshonly => true, # Only run this exec resource when notified (when file content changes)
}
