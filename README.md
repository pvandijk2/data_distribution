# data_distribution
Infrastructure for data distribution network

# Host setup using raspbian
* Image raspbian minimal image to SD card and boot
* Reserve an IP for the rpi MAC
* Set up port forwarding of 22, 8080, 60000-61000 in the router to the rpi
* Install applications: 
'''sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common docker-ce vim git'''
* Add pi user to docker group: 
'''sudo groupadd docker;sudo gpasswd -a $USER docker;newgrp docker'''
* Create a jenkins docker image: 
'''docker run -p 8080:8080 -p 50000:50000 -v jenkins:/var/jenkins_home wouterds/rpi-jenkins'''
* TODO: clone this repo and start jenkins image as daemon (includes clone of jenkins settings)
* TODO: Test connectivity to kenkins



# Client Setup
* Image SD with arch Linux image
* Configure image to run ssh on boot and over USB (https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a)
* Configure DuckDNS to use our token and domain name & store logs in /var/log/duckdns dir
* Increase temporary disk size by adding "tmpfs   /tmp         tmpfs   nodev,nosuid,size=2G          0  0" to /etc/fstab (src: https://wiki.archlinux.org/index.php/Tmpfs)
* Create a swap file using the instructions in https://wiki.archlinux.org/index.php/swap
* Generate UTF-8 locales using the instructions from https://wiki.archlinux.org/index.php/locale
* Run the install script install.sh
* Follow arch linux set using https://github.com/phortx/Raspberry-Pi-Setup-Guide
* Install docker using Note: Use the architecture version specified in https://archlinuxarm.org/forum/viewtopic.php?f=31&t=4570
* Clone the this repo and build the JaaS image using docker build -t "jaas" .
* docker run -i -t jaas:latest /bin/bash

