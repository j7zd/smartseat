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
        
    def deinit(self):
        self.pwm.deinit()

class Relay:
    def __init__(self, pin):
        self.pin_num = pin
        self.pin = Pin(pin, Pin.OUT)
        self.pin.value(0)    
    
    def on(self):
        self.pin.value(0)
    
    def off(self):
        self.pin.value(1)
    

def run_toilet():
    from time import sleep
    buttons = Buttoner(69,69) # change
    s180 = Servo180(1, 180)
    s360 = Servo360(0)
    relay = Relay(2)
    relay.off()
    for _ in range(2):
        #lower head
        for i in range(76, 166, 1):
            s180.value(i)
            sleep(0.02)
        relay.on()
        
        sleep(0.4)
        s360.value(-500000)
        sleep(8)
        relay.off()
        sleep(2)
        
        for i in range(166, 76, -1):
            s180.value(i)
            sleep(0.01)
    
        s360.value(0)
        sleep(1)
    
    s180.deinit()
    s360.deinit()
    relay.off()