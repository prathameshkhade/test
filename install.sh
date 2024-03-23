#!/bin/bash

# install dependacies
printf "[+] Installing dependacies...\n"
sleep 1
pip3 install -r requirements.txt

if [[$? == 0]];
then
	sleep 1
	clear
	printf "\n[✓] Installed sucessfully!"
else
	printf "\n[!] Something went wrong!"
	printf "\n[!] Please try again!"
fi
