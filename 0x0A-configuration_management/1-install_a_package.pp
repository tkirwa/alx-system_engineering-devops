# Install Flask package from pip3
package { 'Flask':
  ensure   => '2.1.0',  # Specify the desired version of Flask
  provider => 'pip3',   # Use pip3 as the package provider
}
