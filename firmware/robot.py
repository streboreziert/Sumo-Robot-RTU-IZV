from machine import Pin, PWM
import imu


class Robot:
    
    def __init__(self,i2c):
        print("This is robot")
        
        self.imu = imu.Imu(i2c)
        #self.motor = []
        self.motor = [[PWM(Pin(16),freq=1024,duty_u16=0xFFFF),
                       PWM(Pin(17),freq=1024,duty_u16=0xFFFF)],
                      [PWM(Pin(18),freq=1024,duty_u16=0xFFFF),
                       PWM(Pin(19),freq=1024,duty_u16=0xFFFF)]]

    
    def deinit(self):
        self.stop()
        self.imu.stop()
        
    def drive(self, left, right):
        self.__driveMotor(0,-left)
        self.__driveMotor(1,right)
        
    def turn(self, angle, speed):
        self.imu.resetAngle()
        err = angle
        
        while abs(err) > 5:
            sp = err * 500
            
            # Limit speed
            sp = max(-speed, min(sp, speed));
            
            
            self.drive(int(-sp),int(sp))
            
            # Update error
            err = angle - self.imu.readAngle()
        
        self.stop()
        print(self.imu.readAngle())
    
    def stop(self):
        self.drive(0,0)
        
        
    def __driveMotor(self, mId, speed):        
        if speed > 0:
            if speed > 0xFFFF:
                speed = 0xFFFF
            self.motor[mId][0].duty_u16(0xFFFF)
            self.motor[mId][1].duty_u16(0xFFFF-speed)
        elif speed < 0:
            if speed < -0xFFFF:
                speed = -0xFFFF
            self.motor[mId][1].duty_u16(0xFFFF)
            self.motor[mId][0].duty_u16(0xFFFF+speed)
        else:
            self.motor[mId][0].duty_u16(0xFFFF)
            self.motor[mId][1].duty_u16(0xFFFF)
