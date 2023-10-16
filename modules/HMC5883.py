from machine import Pin, SoftI2C
from time import sleep
import math
import os

HMC5883_ADDR = 0x0D
DB5883_SETUP_ADDR = 0x09
DB5883_READ_ADDR = 0x00

#machine = os.uname().machine
i2c1 = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100_000)

def setup():
    #i2c1.writeto_mem(HMC5883_ADDR, 0x02, b'\x00') ##Set (0x02 Register) mode to Continuous (00)
    i2c1.writeto_mem(HMC5883_ADDR, DB5883_SETUP_ADDR, b'\x00')

def b2i(x, y):
    return (x << 8 | y) if not x & 0x80 else (-(((x ^ 255) << 8) | (y ^ 255) + 1))

def raw():
    #d = i2c1.readfrom_mem(HMC5883_ADDR, 0x03, 6)
    d = i2c1.readfrom_mem(HMC5883_ADDR, DB5883_READ_ADDR, 6)
    x = b2i(d[0], d[1]) * 0.92 * 0.1 # mG to uT
    y = b2i(d[2], d[3]) * 0.92 * 0.1
    z = b2i(d[4], d[5]) * 0.92 * 0.1 
    s = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
    return (x, y, z, s)

xMax = -99999
xMin = 99999
yMax = -99999
yMin = 99999
def heading():
    x, y, z, s = raw()
    heading = math.atan2((y - ((yMax + yMin) / 2.0)), (x - ((xMax + xMin) / 2.0)))
    if heading < 0:
        heading += 2 * math.pi
    if heading > 2 * math.pi:
        heading -= 2 * math.pi
    #return heading * 180 / math.pi
    return 5

def calibrate():
    global xMax, xMin, yMax, yMin
    import display, switch
    display.scroll("CALIBRATE COMPASS")
    display.scroll("PRESS S1 TO STOP")
    while not switch.value(switch.S1):
        x, y, z, s = raw()
        xMax = max(xMax, x)
        yMax = max(yMax, y)
        xMin = min(xMin, x)
        yMin = min(yMin, y)
        sleep(0.05)
    display.scroll("FINISH")

setup()
