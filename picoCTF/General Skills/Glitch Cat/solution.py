 #!/usr/bin/env python3

from subprocess import Popen, PIPE

# collect the raw flag from the server, forced timeout connection
command = 'nc -i 1 saturn.picoctf.net 65353'

# Execute the command in python, keep only standard output, do not open a new shell
get_flag = Popen(command.split(), stderr=None, stdout=PIPE, shell=False)
stdout = get_flag.communicate()

# parse the flag and split it into a list of chunks
flag_chunks = stdout[0].decode().replace('\'', '').split(' + ')

# reuild the flag, as one liner
flag = ''.join(chr(int(i[+4:-1], 0)) if 'chr' in i else i for i in flag_chunks)

# same in expanded synthax
flag = ''
for i in flag_chunks:
  if 'chr' in i:
    flag += chr(int(i[+4:-1], 0))   # cut the hex value out of the raw string, cast it into integer and conver it back to char
  else:
    flag += i                       # the first and last parts of the flag are kept

print(flag)
