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

'''
conn.setDelegate( MyDelegate() )
 
service_uuid = bluepy.btle.UUID(BLE_SERVICE_UUID)
ble_service = conn.getServiceByUUID(service_uuid)

uuidConfig = bluepy.btle.UUID(BLE_CHARACTERISTIC_UUID)
data_chrc = ble_service.getCharacteristics(uuidConfig)[0]
'''

'''
services_dic = conn.getServices()

print("Services......")
for service in services_dic:
    print(service.uuid)


charac_dic = service.getCharacteristics()


print("Characteristic......")
for charac in charac_dic:
    print(charac.uuid)
'''

services_dic = conn.getServiceByUUID('00001523-1212-efde-1523-785feabcd123')
charac_dic = services_dic.getCharacteristics()[0]
#print(charac_dic.uuid)

data = charac_dic.read()
print('Get data:',data)
#print('len of  data:',len(data))

#try:
#    charac_dic = services_dic.getCharacteristics()[0]
#    while 1:
#       val = binascii.b2a_hex(charac_dic.read())

#val = binascii.b2a_hex(data)
#val = binascii.unhexlify(val)
#val = struct.unpack('f', val)[0]
#print (str(val) + " deg C")

#       time.sleep(1)

#finally:
#     conn.disconnect()

#temp_uuid = UUID(0x1524)


#charac_dic = service.getCharacteristics()


#print("Characteristic......")
#for charac in charac_dic:
#    print(charac.uuid)


#data = charac.read() #read data

#data = data[0]
#print('Get data:',data)

