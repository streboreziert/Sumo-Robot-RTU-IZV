import vl53l0x
from machine import Pin, PWM, ADC, I2C
import neopixel
import time
import robot
from machine import Pin ,PWM
from machine import Pin, I2C
from imu import Imu
import neopixel
import robot

np = neopixel.NeoPixel(Pin(14), 6)
buzzer = PWM(Pin(25), duty_u16=0)
ir = PWM(Pin(5), freq=38000, duty_u16=0x8000)
senL = Pin(35, Pin.IN, Pin.PULL_UP)
senFL = Pin(34, Pin.IN, Pin.PULL_UP)
senR = Pin(4, Pin.IN, Pin.PULL_UP)
senFR = Pin(23, Pin.IN, Pin.PULL_UP)

a=0
b=0
c=0
d=0

i2c1 = I2C(1, sda=Pin(21), scl=Pin(22), freq=400000)
rob = robot.Robot(i2c1)

i2c = I2C(0, sda=Pin(32), scl=Pin(33), freq=400000)
tof = vl53l0x.VL53L0X(i2c)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)

def neosen(which,numb):
    
     if which==0:
        np[numb]=(200,0,0)
        np.write()
     if which==1:
        np[numb]=(0,0,0)
        np.write()
    
tof.start()
while True:
    buzzer.freq(500)
    buzzer.duty_u16(32767) 
    a=senL.value()
    b=senFL.value()
    c=senR.value()
    d=senFR.value()
    distance = tof.read()
    neosen(a,1)
    neosen(b,2)
    neosen(c,4)
    neosen(d,3)
        
    if(distance < 8190):
          print('Distance: ', tof.read())
