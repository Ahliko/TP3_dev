from sys import argv
from os import system

if len(argv) <= 1:
    print(system(f"ping {input('Enter an Ip or Domain Name : ')} -c 2"))
else:
    print(system(f"ping {argv[1]} -c 2"))
