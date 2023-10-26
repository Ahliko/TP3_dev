import os
from sys import argv


def ping(host):
    if os.system(f"ping -c 1 {host} > /dev/null 2>&1") == 0:
        print("UP !")
    else:
        print("DOWN !")


if len(argv) <= 1:
    ping(argv[input('Enter an Ip or Domain Name : ')])
else:
    ping(argv[1])
