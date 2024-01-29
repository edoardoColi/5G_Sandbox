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

echo -e "${YELLOW}Do you want to Install Docker?: [Y/n]${DEFAULT}"
read -r confirmation
if [[ ! "$confirmation" =~ ^[Nn]|[Nn][Oo]$ ]]; then
	echo "Installing..."
	if [ $(dpkg -l | grep -c "docker-c" ) -eq 0 ]; then
		sudo apt-get install -y \
			ca-certificates \
			curl \
			gnupg \
			lsb-release \
			make

		echo -e "${BLUE}Adding Docker's official GPG key${DEFAULT}"
			sudo mkdir -m 0755 -p /etc/apt/keyrings
			curl -fsSL  https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

			echo \
			"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
			$(. /etc/os-release && echo $VERSION_CODENAME) stable" | \
			sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

			sudo apt-get update -y
			sudo apt-get install -y \
				docker-ce \
				docker-ce-cli \
				containerd.io \
				docker-compose-plugin \
				docker-compose

		echo -e "${BLUE}Test Docker installation${DEFAULT}"
			sudo docker run hello-world
			if [ $? -ne 0 ]; then
				echo -e "${RED}  \"Something went wrong with Docker Installation\"${DEFAULT}"
			else
				echo -e "${GREEN}  \"All Docker dependencies Installed\"${DEFAULT}"
			fi

		echo -e "${BLUE}Make Docker run as root${DEFAULT}"
			sudo groupadd docker
			sudo usermod -aG docker $USER
			newgrp docker

		echo -e "${BLUE}Test Docker installation without sudo${DEFAULT}"
			docker run hello-world
			if [ $? -ne 0 ]; then
				echo -e "${RED}  \"Something went wrong with Docker run as root\"${DEFAULT}"
			else
				echo -e "${GREEN}  \"Now docker runs as root\"${DEFAULT}"
			fi
	else
		echo -e "${GREEN}  \"Some packets like 'docker-c*' installed, seems Docker is already Installed\"${DEFAULT}"
	fi
else
	echo "You choose no"
fi

echo -e "${YELLOW}Do you want to Remove Docker?: [y/N]${DEFAULT}"
read -r confirmation
if [[ "$confirmation" =~ ^[Yy]|[Yy][Ee][Ss]$ ]]; then
	echo -e "${RED}Are you sure to Remove Docker?: [y/N]${DEFAULT}"
	read -r confirmationagain
	if [[ "$confirmationagain" =~ ^[Yy]|[Yy][Ee][Ss]$ ]]; then
		echo "Removing..."
		echo "TODO"
# Complete Clean-up(da controllare se va bene) e da aggiungere il resto
#		echo -e "${BLUE}Doing a complete Cleanup${DEFAULT}"
#			sudo apt remove docker-desktop
#			rm -r $HOME/.docker/desktop
#			sudo rm /usr/local/bin/com.docker.cli
#			sudo apt purge docker-desktop
	else
		echo "Not Removing"
	fi
else
	echo "Not Removing"
fi

exit 0
