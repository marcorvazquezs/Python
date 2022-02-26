#!/bin/bash

# Author:                         Marco Vazquez
# Date of latest revision:        2/25/2022
# Purpose:                        Timestamp a log file

# Declare a functions
year=`date +%Y`
month=`date +%m`
day=`date +%d`
hour=`date +%H`
minute=`date +%M`
second=`date +%S`
weekday=`date +%A`
fulldate=`date +%D`
fulltime=`date +%r`
current_date_time=$fulldate-$hour:$minute
# Declare functions

# Main
echo "The full date and time is $current_date_time"

echo "At $hour:$minute, the script copies the syslog to the current working directory"
cp /var/log/syslog syslog.$year$month$day




