#!/usr/bin/env python3

import datetime
import read_sensor
import time

def sensor_readings_to_csv():

    current_time = datetime.datetime.now()
    hex_byte_readings = read_sensor.get_reading() # list
    temperature = read_sensor.convert_temperature_reading(eval(hex_byte_readings[0]), eval(hex_byte_readings[1]), 'c') #string
    humidity = read_sensor.convert_humidity_reading(eval(hex_byte_readings[3]), eval(hex_byte_readings[4])) #string

    sensor_readings_file = open('sensor_readings_file.txt', 'a')
    sensor_readings_file.write("{0}, {1}, {2}\n".format(current_time, temperature, humidity))
    sensor_readings_file.close()


if __name__ == "__main__":
	for i in range(20):
		sensor_readings_to_csv()
		time.sleep(0.5)

