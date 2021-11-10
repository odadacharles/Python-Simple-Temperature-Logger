import serial
from datetime import datetime
import csv

Temperature = ""
Dataline =[]
serialPort = serial.Serial(port = "COM7", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)



serialPort.close()
serialPort.open() #Open the serial port

while(1):
    #Wait until there is data in the serial buffer

    if(serialPort.in_waiting>0):
        f = open('C:/Users/aolch/Documents/Python Simple Temperature Logger/Kisumu-temperature-humidity.csv', 'w')
        writer=csv.writer(f)
        Time = datetime.now()
        #Read data out of the buffer until a carriage return/new line is found and save to the variable "Temperature"
        T=str(serialPort.readline() )
        #print(T)
        Temperature=T[2:7]
        Humidity = T[8:13]
        #print(str(Time)+str(Temperature))
        
        print(Temperature)
        print(Humidity)
        #Dataline.append(Time)
        # Dataline.append(Temperature)
        # Dataline.append(Humidity)
        # print(Dataline)
        #writer.writerows(Dataline)
        #Dataline=[]
        #writer.writerows(Temperature)
        #f.close()
serialPort.close()