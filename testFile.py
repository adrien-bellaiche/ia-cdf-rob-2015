__author__ = 'adrie_000'

from time import sleep

import serial as ser


out = ser.Serial(port='COM4', baudrate=115200)
print 'Serial port opened'
sleep(1)
out.write('#19 P700 \n')
out.flush()
print 'command sent'
sleep(5)
out.write('#19 P2300 \n')
print 'second command sent'
sleep(5)
print 'closing serial link'
out.close()
