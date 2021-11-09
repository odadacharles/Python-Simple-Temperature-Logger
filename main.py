import serial
from datetime import datetime
import csv

Temperature = ""
serialPort = serial.Serial(port = "COM7", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)



serialPort.close()
serialPort.open() #Open the serial port

while(1):
    #Wait until there is data in the serial buffer

    if(serialPort.in_waiting>0):
        f = open('C:/Users/aolch/Documents/Python Simple Temperature Logger/Kisumu-temperature-humidity.csv', 'w')
        writer=csv.writer(f)
        Time = str(datetime.now())
        #Read data out of the buffer until a carriage return/new line is found and save to the variable "Temperature"
        Temperature=str(serialPort.readline() )
        print(Time)
        print(Temperature)
        writer.writerow(Time)
        writer.writerow(Temperature)
        f.close()
serialPort.close()