#!/bin/bash
VERSION=V4
# This script will run after an update has been downloaded from the repo. It must check for changes in the update file or in version number. Update script will have version number on first line in order to compare easily.

# Read old file to check version. Store in OLDVERSION.

#Compare Versions using string comparisons. Will only check if different not if different not if older or newer.
OLDVERSION=$(sed -n '2p' ~/Updates/UpdateScriptTest.sh)
echo $VERSION
echo ${OLDVERSION:8}

if [ ${OLDVERSION:8} == $VERSION ]; then
	echo "Software is up to date. No need to install."
else
	echo "New Version Available. Installing."
	#Do other things here. Such as write to file, over write, run script.
	#Currently set to reboot after 10 mins. This gives time for everything to complete.
	cp -f ~/InitialDevBM/Updates/UpdateScriptTest.sh ~/Updates/UpdateScriptTest.sh
	echo "OTA update succesfull! Version V4 Now installed."
	sudo shutdown -r 2 "Rebooting in 2 minutes to apply Update."
fi


