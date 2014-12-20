__author__ = 'adrie_000'

from time import sleep
from SerialCom import HokuyoCom, find_ports

ports = find_ports()
com = HokuyoCom(ports[0])
sleep(0.2)
[ranging, angles] = com.get_fresh_data()
print len(ranging), len(angles)