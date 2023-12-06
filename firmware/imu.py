from machine import Pin, PWM, I2C, Timer
from micropython import const


class Imu:
    
    # Gyro Full scale options (deg/s)
    GYRO_FS__250  = const(0)
    GYRO_FS__500  = const(1)
    GYRO_FS__1000 = const(2)
    GYRO_FS__2000 = const(3)
    
    
    def __init__(self, i2c, gyroFs=GYRO_FS__1000):
        self.i2c = i2c
        print(self.i2c.scan())
        
        self.i2c.writeto(104, bytearray([107, 0]))
        
        # Set 1000 deg/s
        # 0x00 - 250 deg/s
        # 0x08 - 500 deg/s
        # 0x10 - 1000 deg/s
        # 0x18 - 2000 deg/s
        kGyroFsConfig = [0x00, 0x08, 0x10, 0x18]
        kGyroFs = [250.0, 500.0, 1000.0, 2000.0]

        self.i2c.writeto(104, bytearray([0x1B, kGyroFsConfig[gyroFs]]))
        self.fs = kGyroFs[gyroFs]
        
        self.angle = 0.0
        
        self.timer = Timer(-1)
        self.timer.init(period=10, mode=Timer.PERIODIC, callback=self.updateAngle)
        
    def readAngle(self):
        return self.angle
    
    def resetAngle(self):
        self.angle=0.0
    
    def updateAngle(self, t):
        a = self.i2c.readfrom_mem(104, 71, 2)
        value = self.bytes_toint(a[0], a[1])            
        if value < 80 and value > -80:
            value = 0
        dps = self.fs * value / 0x8000
        self.angle += dps * 0.01
        
    def stop(self):
        self.timer.deinit()
        
        
    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)
    
