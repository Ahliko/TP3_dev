from psutil import net_if_addrs

print(net_if_addrs()["wlp4s0"][0][1])