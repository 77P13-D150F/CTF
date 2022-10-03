#!/usr/bin/bash

#chmod +x static
chmod +x ltdis.sh

# one liner
# ltdis.sh static || strings static | grep picoCTF

# extended
ltdis.sh static

if [[ $? == 0 ]]; then
  cat static.ltdis.strings.txt | grep picoCTF
else
  strings static | grep picoCTF
fi

exit 0
