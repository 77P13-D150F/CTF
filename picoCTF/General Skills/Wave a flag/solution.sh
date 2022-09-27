#!/usr/bin/bash

chmod +x warm
warm -h 2>/dev/null

if [ $? -ne 0 ]; then
  strings warm | grep picoCTF
fi

exit 0
