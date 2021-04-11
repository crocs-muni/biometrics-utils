#!/bin/bash

echo "Provision script."

# Update the system and install necessary software
apt update
apt -y upgrade
apt -y install vim git build-essential curl
apt -y install python3-pip

# Install Visual studio Code
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
rm packages.microsoft.gpg
apt -y install apt-transport-https
apt update
apt -y install code

# Download the homework files
cd /home/vagrant/
mkdir -p Documents
chown -R vagrant:vagrant /home/vagrant/Documents
cd Documents
runuser -u vagrant git clone https://github.com/crocs-muni/biometrics-utils.git
cd biometrics-utils
runuser -u vagrant make install

# Reboot to apply updates
reboot
