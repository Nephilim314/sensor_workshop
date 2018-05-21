#!/usr/bin/env python3

import numpy as np

def min_max_avg():
    temperature = []
    humidity = []
    sensor_readings_file = open('sensor_readings_file.txt', 'r')
    line = sensor_readings_file.readline()
    while line:
        splitted_line = line.split(',')
        #print("Date & Time: {0}\nTemperature: {1}\nHumidity: {2}".format(splitted_line[0], splitted_line[1], splitted_line[2]))
        temperature.append(float(splitted_line[1]))
        humidity.append(float(splitted_line[2]))
        line = sensor_readings_file.readline()

    min_temperature = min(temperature)
    max_temperature = max(temperature)
    avg_temperature = np.mean(temperature)

    min_humidity = min(humidity)
    max_humidity = max(humidity)
    avg_humidity = np.mean(humidity)

    print("Temperature:: Min: {0}, Max: {1}, Average: {2}".format(min_temperature, max_temperature, avg_temperature))
    print("Humidity:: Min: {0}, Max: {1}, Average: {2}".format(min_humidity, max_humidity, avg_humidity))

if __name__ == "__main__":
    min_max_avg()