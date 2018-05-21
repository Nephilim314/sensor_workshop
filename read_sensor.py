#!/usr/bin/env python3

import smbus
import RPi.GPIO as GPIO
import time

LED_PIN = 20
GPIO_IS_SETUP = False
DEVICE_ADDRESS = 0x44 # the I2C address of our SHT-31 sensor

bus = smbus.SMBus(1)

def setup_gpio():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED_PIN, GPIO.OUT)
	GPIO_IS_SETUP = True
	print("Setting up GPIO")

def led_on():
	if not GPIO_IS_SETUP:
		setup_gpio()
	GPIO.output(LED_PIN, 1)

def led_off():
	if not GPIO_IS_SETUP:
		setup_gpio()
	GPIO.output(LED_PIN, 0)

def get_status():
	bus.write_byte_data(DEVICE_ADDRESS, 0xF3, 0x2D)
	block = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, 3)
	print("Status MSB: " + hex(block[0]))
	print("Status LSB: " + hex(block[1]))

def clear_status():
	bus.write_byte_data(DEVICE_ADDRESS, 0x30, 0x41)
	print("Status register was cleared")
	
def soft_reset():
	bus.write_byte_data(DEVICE_ADDRESS, 0x30, 0xA2)
	print("Soft reset was done")

def get_reading():
	bus.write_byte_data(DEVICE_ADDRESS, 0x24, 0x00)
	time.sleep(0.015)
	block = bus.read_i2c_block_data(DEVICE_ADDRESS, 0, 6)
	new_block = []
	for i in block:
		new_block.append(hex(i))
	return new_block

def convert_temperature_reading(t_msb, t_lsb, mode='c'):
	t_msb = t_msb << 8
	raw_temperature = t_msb | t_lsb
	print("Temperature"+hex(raw_temperature))
	temp_f = -49 + 315*(raw_temperature/(2**16-1))
	temp_c = -45 + 175*(raw_temperature/(2**16-1))
	if mode=='c':
		return temp_c
	if mode=='f':
		return temp_f

def convert_humidity_reading(h_msb, h_lsb):
	h_msb = h_msb << 8
	raw_humidity = h_msb | h_lsb
	print("Humidity"+hex(raw_humidity))
	humidity = 100 * (raw_humidity/(2**16-1))
	return humidity

a_t_c = convert_temperature_reading(0x5f, 0xe6, mode='c')
b_t_c = convert_temperature_reading(0x5f, 0xf6, mode='c')
c_t_c = convert_temperature_reading(0x5f, 0x4e, mode='c')
print(a_t_c, b_t_c, c_t_c)

a_t_f = convert_temperature_reading(0x5f, 0xe6, mode='f')
b_t_f = convert_temperature_reading(0x5f, 0xf6, mode='f')
c_t_f = convert_temperature_reading(0x5f, 0x4e, mode='f')
print(a_t_f, b_t_f, c_t_f)

a_h = convert_humidity_reading(0x77, 0x8a)
b_h = convert_humidity_reading(0x76, 0xdf)
c_h = convert_humidity_reading(0x78, 0x20)
print(a_h, b_h, c_h)

#for x in range(0, 10):
#	led_on()
#	time.sleep(0.25)
#	led_off()
#	time.sleep(0.25)

#get_status()
#print(get_reading())
#clear_status()
#soft_reset()
#get_status()
