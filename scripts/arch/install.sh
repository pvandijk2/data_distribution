#!/bin/bash
sed -i 's/#Color/Color/' /etc/pacman.conf
pacman -Sy --noconfirm sudo

for arg in 'archlinux-keyring' 'pacman' 'ntp' 'slang' 'vim' 'filesystem' 'wget' 'base-devel' 'yajl' 'mosh'
do
	sudo pacman -Sy --noconfirm $arg
	if [ $? -ne 0 ] 
	then
		echo "$arg failed to install and had return code: $?"
		exit
	fi

done

sudo pacman-key --init
sudo pacman-key --populate archlinux
sudo rm /etc/ssl/certs/ca-certificates.crt
sudo pacman -Syu --noconfirm --ignore filesystem
sudo pacman -S --noconfirm filesystem --force

sudo systemctl enable ntpd.service
sudo systemctl start ntpd.service

wget https://aur.archlinux.org/cgit/aur.git/snapshot/package-query.tar.gz
tar -xvzf package-query.tar.gz
cd package-query && makepkg -si

wget https://aur.archlinux.org/cgit/aur.git/snapshot/yaourt.tar.gz
tar -xvzf yaourt.tar.gz
cd yaourt && makepkg -si

#ntp
#package-query
#--needed wget base-devel yajl
#slang
#sudo
#vim
#vi
#filesystem --force
#sed -i 's/#Color/Color/' /etc/pacman.conf
#pacman -S filesystem --force
#pacman -S yaourt
#vim /etc/pacman.conf
#vi /etc/pacman.conf
#pacman -S yaourt
#pacman -Sy pacman
#vi /etc/pacman.conf
#pacman -Sy pacman
#pacman-key --init
#pacman -S archlinux-keyring
#pacman-key --populate archlinux
#pacman -Syu --ignore filesystem
#pacman -S wget
#pacman -S newt
#pacman -S vim
