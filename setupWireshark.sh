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

echo -e "${YELLOW}Do you want to Install Wireshark?: [Y/n]${DEFAULT}"
read -r confirmation
if [[ ! "$confirmation" =~ ^[Nn]|[Nn][Oo]$ ]]; then
	echo "Installing..."

	if [ $(dpkg -l | grep -c "wireshark " ) -eq 0 ]; then
		echo -e "${BLUE}Adding Wireshark's PPA stable${DEFAULT}"
		sudo add-apt-repository -y ppa:wireshark-dev/stable
		sudo apt-get update -y

		sudo apt-get install -y \
			wireshark \
			tshark

		echo -e "${BLUE}Adding User to wireshark group to run as root if in wireshark-common said <YES>${DEFAULT}"
			sudo groupadd wireshark
			sudo usermod -aG wireshark $USER
			newgrp wireshark

	else
		echo -e "${GREEN}  \"Some packet like 'wireshark ' installed, seems Wireshark is already Installed\"${DEFAULT}"
	fi
else
	echo "You choose no"
fi

echo -e "${YELLOW}Do you want to Remove Wireshark?: [y/N]${DEFAULT}"
read -r confirmation
if [[ "$confirmation" =~ ^[Yy]|[Yy][Ee][Ss]$ ]]; then
	echo -e "${RED}Are you sure to Remove Wireshark?: [y/N]${DEFAULT}"
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
