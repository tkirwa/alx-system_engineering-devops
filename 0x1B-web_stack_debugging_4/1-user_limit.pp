# This Puppet script increases the file limits for the holberton user in order to
# prevent errors when logging in and opening files.

# This exec resource modifies the hard file limit for the holberton user.
# It uses the 'sed' command to locate the line containing 'holberton hard' in the limits.conf file
# and replaces the current value ('5') with a higher value ('50000').
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# This exec resource modifies the soft file limit for the holberton user.
# It uses the 'sed' command to locate the line containing 'holberton soft' in the limits.conf file
# and replaces the current value ('4') with a higher value ('50000').
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
