#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CamJam EduKit 2 - Sensors
# Worksheet 3 - Temperature

##### Modules #####
import os
import glob
from time import sleep
import subprocess
import wget

##### Variables #####
# Finds the correct device file that holds the temperature data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Initialize the GPIO Pins
os.system('modprobe w1-gpio')  # Turns on the GPIO module
os.system('modprobe w1-therm') # Turns on the Temperature module
# ---->

##### Fonctions #####

# A function that reads the sensors data
def read_temp_raw():
    f = open(device_file, 'r') # Opens the temperature device file
    lines = f.readlines() # Returns the text
    f.close()
    return lines

# Convert the value of the sensor into a temperature
def read_temp():
    lines = read_temp_raw() # Read the temperature 'device file'

    # While the first line does not contain 'YES', wait for 0.2s
    # and then read the device file again.
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()

    # Look for the position of the '=' in the second line of the
    # device file.
    equals_pos = lines[1].find('t=')


    # If the '=' is found, convert the rest of the line after the
    # '=' into degrees Celsius, then degrees Fahrenheit
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = round(float(temp_string) / 1000.0,1)
#         temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

def ds18b20(sonde):
	return (read_temp(),sonde,'temperature')

# ---->

# test des deux fonctions
if __name__ == "__main__":
	# Print out the temperature until the program is stopped.
# 	while True:

	data = ds18b20('ds18b20')
	print(str(data[0]),'°C',sep=' ')
# 	sleep(1)
