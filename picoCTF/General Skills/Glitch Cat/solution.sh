#!/usr/bin/bash

# donwload the string and remove the quotes
flag=$(nc -i 1 saturn.picoctf.net 65353 2>/dev/null | sed -e "s/[']//g")

# divide the string into an array of strings, separated by ' + '
IFS_log=$IFS
IFS=' + '
read -a arr <<< "$flag"
IFS=$IFS_log

# rebuld the flag, converting the hex digits into ascii
flag=''
for chunk in ${arr[@]}; do
        if [[ $chunk == *chr* ]]; then
                hex=$(echo $chunk | sed -e "s/[chr(0x)]//g")  # remove the extra characters from the hex number
                flag+=$(echo -e "\x$hex")                     # rebuld the hex number and convert it into ascii
        else
                flag+=$chunk                                  # keep the first and last parts
        fi
done
echo $flag

exit 0
