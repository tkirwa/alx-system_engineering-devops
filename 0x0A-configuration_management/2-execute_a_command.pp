# Execute a command to kill a process named "killmenow"
exec { 'killmenow':
  command     => 'pkill -f killmenow',  # Specify the command to execute using pkill to kill the process
  path        => '/usr/bin',            # Set the path to the location of the pkill command
  refreshonly => true,                  # Ensure the exec resource is only triggered when explicitly refreshed
}
