import serial #import the serial port library
from datetime import datetime #import the library for getting current time
import time #import the library for converting current time to unix time
import csv #import the csv library for writing to the csv file
import sys #import the sys library that is needed by the sys.exit() feature to close the program

Dataline =[] #create an empty list called "Dataline" to hold a single row of data
readings = 0
#initialize the serial port reader by specifying the parameter of the serial port the data will be coming in from
serialPort = serial.Serial(port = "COM5", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


serialPort.close() #close the serial port to end other instances that may still be running in the background
serialPort.open() #Open the serial port

while (readings<10): 
    #Wait until Ten reading have been collected


    if(serialPort.in_waiting>0):
        f = open('C:/Users/Charlie.O/Documents/Python Projects/Python-Simple-Temperature-Logger/Kisumu-temperature-humidity.csv', 'a',newline='') #open the csv file that will be written to. 'a' worked, 'w' did not
        writer=csv.writer(f) #create an instance of the csv writer that will be writing to the file 'f'
        Time = datetime.now() #Get the current date and time
        UnixTime = str(time.mktime(Time.timetuple())) #convert the current date and time to unixtime. Makes writing to csv less 'clanky'
        #Read data out of the buffer until a carriage return/new line is found and save to the variable "Temperature"
        
        T=str(serialPort.readline() ) #Convert the input from the serial port to string and save to a variable
        Temperature=T[2:7] #Isolate the temperature from the serial port reading
        Humidity = T[8:13] #Isolate the humidity from the serial port reading
       
        Dataline.append(UnixTime) #Append the Unixtime to the Dataline list
        Dataline.append(Temperature) #Append the Temperature to the Dataline list
        Dataline.append(Humidity) #Append the Humidity to the Dataline list
        print(Dataline) #Print the Dataline list to confirm there is a reading 
        writer.writerows([Dataline]) #Write the values of Dataline list to the csv file as a list of lists. A simple list will result in each character being separated by a comma
        readings+=1
        Dataline=[] #Reinitialize the dataline list in preparation for the next reading

serialPort.close() #Close the serial port
input("Press Enter to exit: ") #Prompt the user to press enter to manually exit the program
sys.exit()        

