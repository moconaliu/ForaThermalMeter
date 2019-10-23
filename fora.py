import bluepy
#import UUID
from bluepy.btle import UUID

import binascii
import struct

# Address of BLE device to connect to.
#BLE_ADDRESS = "c0:26:df:04:a3:83"
# BLE heart rate service
#BLE_SERVICE_UUID ="00001523-1212-efde-1523-785feabcd123"
# H notifies.
#BLE_CHARACTERISTIC_UUID= "00002a37-0000-1000-8000-00805f9b34fb";

'''
class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self):
        bluepy.btle.DefaultDelegate.__init__(self)
        # ... initialise here

    def handleNotification(self, cHandle, data):
    	data = bytearray(data)
    	#print 'Developer: do what you want with the data.'
        #print data
'''


scanner = bluepy.btle.Scanner()
devices = scanner.scan(timeout=3)
print('Found %d devices' % (len(devices)))

for dev in devices:
    print()
    print('Name: ',dev.getValueText(9))
    print('Address: ', dev.addr)

addr = 'c0:26:df:04:a3:83'
print("start connecting to Fora TD-1241")

conn = bluepy.btle.Peripheral(addr,"random")
print("connected.....")
