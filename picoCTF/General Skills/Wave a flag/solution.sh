#!/usr/bin/bash

chmod +x warm

# one liner
# warm -h 2>/dev/null || strings warm | grep picoCTF

# extended
warm -h 2>/dev/null

if [ $? -ne 0 ]; then
  strings warm | grep picoCTF
fi

exit 0
