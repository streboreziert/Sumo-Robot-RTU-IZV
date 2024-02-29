import vl53l0x
from machine import Pin, PWM, ADC, I2C
import neopixel
import time
import robot
from imu import Imu

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

def neosen(which,numb):
    
     if which==0:
        np[numb]=(200,0,0)
        np.write()
     if which==1:
        np[numb]=(0,0,0)
        np.write()

while True:
    l=senL.value()
    fl=senFL.value()
    r=senR.value()
    fr=senFR.value()
    
    if r==1 and l==1 :
            rob.stop()
    elif r==0:
        rob.drive(20000,0)
        
    elif l==0:
        rob.drive(0,20000)
    elif fl==0 and fr==1:
        rob.drive(0,20000)
    elif fr==0 and fl==1:
         rob.drive(20000,0)
    elif fl==0 and fr==0:
        rob.drive(20000,20000)
      
    neosen(l,1)
    neosen(fl,2)
    neosen(r,4)
    neosen(fr,3)
    time.sleep(0.00001)
