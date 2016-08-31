#!/bin/sh

# Network Testing Appliance
# Uses the speedtest.net servers and SpeedTest-CLI
# SpeedTest-cli by Matt Martz

# Version 1 - Simple Speed Testing
# Weekly Email Script

filename=speedtest.txt
filedir=/home/pi/speedtest-cron
current_time=$(date "+%Y.%m.%d-%H.%M.%S")
zipname=$filedir/$current_time.speedtest.zip
email_addresses="email@email.com email@email2.com"

if [ -e "$filedir/$filename" ]
then
   # First lets cleanup all the weeks text files into a zip
   zip $zipname *.speedtest.txt
   # Now remove all those files
   rm *.speedtest.txt -f
   # Now lets email that attachment so we havew a copy of it
   mpack -s "Weekly Speedtesting Archive" $zipname $email_addresses
fi
