# from pymodbus.client import ModbusTcpClient
# client = ModbusTcpClient('127.0.0.1') # Create client(Master) object
# client.connect()                      # connect to device, reconnect automatically
# client.write_coil(1, True)            # set information in device
# result = client.read_coils(1,1)       # get information from device (get the value of address 1 from device 1 (slave))
# print(result.bits[0])                 # use information
# client.close()                        # Disconnect device

# Modbus client
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
import time

print('Start Modbus Client')
client = ModbusClient(host='127.0.0.1', port=502) 
reg=0; address=0

# initialize data
data = [0.1,1.1,2.1,3.1,4.1]

for i in range(10):
   print('-'*5,'Cycle ',i,'-'*30)
   time.sleep(1.0)

   # increment data by one
   for i,d in enumerate(data):
      data[i] = d + 1

   # write holding registers (40001 to 40005)
   print('Write',data)
   builder = BinaryPayloadBuilder(byteorder=Endian.Big,\
                                  wordorder=Endian.Little)
   for d in data:
      builder.add_16bit_int(int(d))
   payload = builder.build()
   result  = client.write_registers(int(reg), payload,\
              skip_encode=True, unit=int(address))

   # read holding registers
   rd = client.read_holding_registers(reg,len(data)).registers
   print('Read',rd)

client.close()