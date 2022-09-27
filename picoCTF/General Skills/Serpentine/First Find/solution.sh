#!/usr/bin/bash

unzip files.zip 1>/dev/null
flag=$(find . -name uber-secret.txt)
cat $flag

exit 0
