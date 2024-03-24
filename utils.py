from machine import Pin, PWM

class Servo360:
    def __init__(self, pin, initial=0):
        self.pwm = PWM(Pin(pin), freq=50)
        self.value(initial)
            
    def value(self, v):
        assert v <= 500000, 'invalid value'
        assert v >= -500000, 'invalid value'
    
        self.pwm.duty_ns(1500000 + v)
        
    def deinit(self):
        self.pwm.deinit()
        
class Servo180:
    def __init__(self, pin, initial=0):
        self.pwm = PWM(Pin(pin), freq=50)
        self.value(initial)
        
    def value(self, v):
        assert v>=0
        assert v<=180
        
        self.pwm.duty_u16(1000 + v * 8000 // 180)
        
    def deinit():
        self.pwm.deinit()
        
if __name__ == '__main__':
    from time import sleep
    s180 = Servo180(1, 180)
    s360 = Servo360(0)
    
    for i in range(76, 166, 1):
        s180.value(i)
        sleep(0.02)
    
    sleep(0.4)
    s360.value(-500000)
    sleep(8)
        
    for i in range(166, 76, -1):
        s180.value(i)
        sleep(0.02)
    
    
    s360.value(0)
    
    s180.deinit()
    s360.deinit()