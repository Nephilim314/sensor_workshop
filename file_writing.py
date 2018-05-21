#!/usr/bin/env python3

import datetime
import read_sensor


def sensor_readings_to_csv():

    current_time = datetime.datetime.now()
    hex_byte_readings = read_sensor.get_reading() # list
    temperature = read_sensor.convert_temperature_reading(hex_byte_readings[0], hex_byte_readings[1], 'c') #string
    humidity = read_sensor.convert_humidity_reading(hex_byte_readings[3], hex_byte_readings[4]) #string

    sensor_readings_file = open('sensor_readings_file.txt', 'w')
    sensor_readings_file.write("{0}, {1}, {2}".format(current_time, temperature, humidity))

    sensor_readings_file.close()


if __name__ == "__main__":
    sensor_readings_to_csv()

