# Python-Simple-Temperature-Logger
This is a simple program that gets data from an Arduino UNO and an AHT10 Temperature/Humidity sensor.
The code included is for the python program that gets the data from the serial port and logs it to a csv file with a Unix timestamp added in python.
The Arduino code is not included. For those interested, the arduino code is simply a modified version of the Adafruit_AHT10_test code. 
I modified the Adafruit code to output the temperature and humidity readings without any labels. 
This makes it easier to extract the data using python code by eliminating unnecessary strings.
The data is highly localised and is collected outdoors in the shade. The rain data is entered manually because I don't have the necessary sensor to collect this data.
