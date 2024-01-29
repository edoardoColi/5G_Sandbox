#!/bin/bash

#Colors
RED="\e[1;31m"
GREEN="\e[1;32m"
YELLOW="\e[1;33m"
BLUE="\e[1;34m"
DEFAULT="\e[0m"

# Check if the script is run with root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root or using sudo."
  exit 1
fi

echo -e "${YELLOW}Do you want to Update the system?: [Y/n]${DEFAULT}"
read -r confirmation
if [[ ! "$confirmation" =~ ^[Nn]|[Nn][Oo]$ ]]; then
	echo "Updating..."
	sudo apt-get update -y
	sudo apt-get upgrade -y
else
	echo "You choose no"
fi

echo -e "${YELLOW}Do you want to Install VirtualBox-7.0?: [Y/n]${DEFAULT}"
read -r confirmation
if [[ ! "$confirmation" =~ ^[Nn]|[Nn][Oo]$ ]]; then
	echo "Installing..."
	if [ $(dpkg -l | grep -c "virtualbox" ) -eq 0 ]; then
		sudo apt-get install -y \
			ca-certificates \
			wget \
			gnupg \
			lsb-release \

		echo -e "${BLUE}Adding Docker's official GPG key${DEFAULT}"
			wget -O- https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo gpg --yes --dearmor -o /usr/share/keyrings/oracle-virtualbox-2016.gpg

			echo \
			"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/oracle-virtualbox-2016.gpg] https://download.virtualbox.org/virtualbox/debian \
			$(. /etc/os-release && echo $VERSION_CODENAME) contrib" | \
			sudo tee /etc/apt/sources.list.d/virtualbox.list > /dev/null

			sudo apt-get update -y
			sudo apt-get install -y \
				linux-headers-$(uname -r) \
				dkms \
				virtualbox-7.0

		echo -e "${BLUE}Make VirtualBox run with Extension Pack${DEFAULT}"
			wget https://download.virtualbox.org/virtualbox/7.0.14/Oracle_VM_VirtualBox_Extension_Pack-7.0.14.vbox-extpack
			sudo vboxmanage extpack install --replace --accept-license=33d7284dc4a0ece381196fda3cfe2ed0e1e8e7ed7f27b9a9ebc4ee22e24bd23c Oracle_VM_VirtualBox_Extension_Pack-7.0.14.vbox-extpack
			rm -f Oracle_VM_VirtualBox_Extension_Pack-7.0.14.vbox-extpack

		echo -e "${BLUE}Make VirtualBox run with admin privileges${DEFAULT}"
			sudo groupadd vboxusers
			sudo usermod -aG vboxusers $USER
			newgrp vboxusers
	else
		echo -e "${GREEN}  \"Some packet like 'virtualbox' installed, seems VirtualBox is already Installed\"${DEFAULT}"
	fi
else
	echo "You choose no"
fi

echo -e "${YELLOW}Do you want Vagrant too?: [y/N]${DEFAULT}"
read -r confirmation
if [[ "$confirmation" =~ ^[Yy]|[Yy][Ee][Ss]$ ]]; then
	echo -e "${BLUE}Adding Vagrant's official GPG key${DEFAULT}"
		wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

		echo \
		"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com \
		$(. /etc/os-release && echo $VERSION_CODENAME) main" | \
		sudo tee /etc/apt/sources.list.d/hashicorp.list
		
		sudo apt-get update -y
		sudo apt-get install -y \
			vagrant
else
	echo "You choose no"
fi
echo -e "${YELLOW}Do you want to Remove VirtualBox?: [y/N]${DEFAULT}"
read -r confirmation
if [[ "$confirmation" =~ ^[Yy]|[Yy][Ee][Ss]$ ]]; then
	echo -e "${RED}Are you sure to Remove VirtualBox?: [y/N]${DEFAULT}"
	read -r confirmationagain
	if [[ "$confirmationagain" =~ ^[Yy]|[Yy][Ee][Ss]$ ]]; then
		echo "Removing..."
		echo "TODO"
		# TODO
	else
		echo "Not Removing"
	fi
else
	echo "Not Removing"
fi

exit 0
