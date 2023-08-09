# Puppet code to fix bad 'phpp' extensions to 'php' in the WordPress file 'wp-settings.php'

# Define an exec resource named 'fix-wordpress'
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php', # Use 'sed' to replace 'phpp' with 'php' in the file
  path    => '/usr/local/bin/:/bin/' # Set the PATH for the command execution
}
