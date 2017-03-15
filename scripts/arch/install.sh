#!/bin/bash
sed -i 's/#Color/Color/' /etc/pacman.conf

for arg in 'archlinux-keyring' 'pacman' 'ntp' 'slang' 'sudo' 'vim' 'filesystem' 'wget' 'base-devel' 'yajl'
do
	sudo pacman -Sy --noconfirm $arg
	if [ $? -ne 0 ] 
	then
		echo "$arg failed to install and had return code: $?"
		exit
	fi

done


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
