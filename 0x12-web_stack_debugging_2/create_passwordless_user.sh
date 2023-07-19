#!/bin/bash

# Check if an argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <username>"
  exit 1
fi

# Create the user without a password
sudo useradd -m -s /bin/bash "$1"

# Set the password to empty
sudo passwd -d "$1"

# Allow the user to run sudo commands without a password
echo "$1 ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/"$1"
sudo chmod 440 /etc/sudoers.d/"$1"
