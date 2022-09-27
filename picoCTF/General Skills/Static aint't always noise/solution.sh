#!/usr/bin/bash

#chmod +x static
chmod +x ltdis.sh

ltdis.sh static

if [[ $? == 0 ]]; then
  cat static.ltdis.strings.txt | grep picoCTF
else
  strings static | grep picoCTF
fi

exit 0
