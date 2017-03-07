# data_distribution
Infrastructure for data distribution network

# Client Setup
* Image SD with arch Linux/Raspbian image
* Configure image to run ssh on boot and over USB (https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a)
* Update/upgrade packages: sudo apt-get update && apt-get upgrade && apt-get dist-upgrade
* Install Docker on Raspbian: sudo curl -sSL https://get.docker.com | sh
* Download Raspbain image: sudo systemctl enable docker && docker run -ti resin/rpi-raspbian:jessie-20160831 /bin/bash
* Install Docker on generic Linux: https://github.com/umiddelb/armhf/wiki/Get-Docker-up-and-running-on-the-RaspberryPi-(ARMv6)-in-four-steps-(Wheezy)
* Configure DuckDNS to use our token and domain name & store logs in /var/log/duckdns dir
