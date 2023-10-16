from machine import Pin
from machine import I2C
from time import sleep
import math
import os

HMC5883_ADDR = 0x0D
DB5883_SETUP_ADDR = 0x09
DB5883_READ_ADDR = 0x00

machine = os.uname().machine
if ("KidBright32" in machine) or ("KidMotor V4" in machine):
    i2c1 = I2C(1, scl=Pin(5), sda=Pin(4), freq=100000)
elif "Mbits" in machine:
    i2c1 = I2C(0, scl=Pin(21), sda=Pin(22), freq=100000)
else:
    i2c1 = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)

def setup():
    #i2c1.writeto_mem(HMC5883_ADDR, 0x02, b'\x00')


setup()
