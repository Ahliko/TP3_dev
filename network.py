import os
from _socket import gethostbyname
from sys import argv

from psutil import net_if_addrs


def lookup(hostname):
    try:
        return gethostbyname(hostname)
    except:
        return "The argument is incorrect !"


def ping(host):
    try:
        if os.system(f"ping -c 1 {host} > /dev/null 2>&1") == 0:
            return "UP !"
        else:
            return "DOWN !"
    except:
        return "The argument is incorrect !"


def ip():
    return net_if_addrs()[[i for i in net_if_addrs()][1]][0][1]


if __name__ == "__main__":
    reponse = ""
    if len(argv) >= 3:
        if argv[1] == "lookup":
            reponse = lookup(argv[2])
        elif argv[1] == "ping":
            reponse = ping(argv[2])
        else:
            reponse = f"'{argv[1]}' is not an available command. Déso."
    elif len(argv) == 2:
        if argv[1] == "ip":
            reponse = ip()
        elif argv[1] == "lookup" or argv[1] == "ping":
            reponse = "You must take two arguments for this function !"
        else:
            reponse = f"'{argv[1]}' is not an available command. Déso."
    else:
        reponse = "Please take an argument !"
    print(reponse)
