# Execute a command to kill the process named "killmenow"

# Define an exec resource named 'pkill'
exec { 'pkill':
  command  => 'pkill killmenow',  # Specify the command to execute, using pkill to kill the process named "killmenow"
  provider => 'shell',            # Use the shell as the provider to execute the command
}
