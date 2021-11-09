import serial
Temperature = ""
serialPort = serial.Serial(port = "COM7", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
open()
Temperature = readline()
print (Temperature)
close()