from webrelay import run_web
from utils import run_toilet

import _thread

class Buttoner:
    def __init__(self, button1_pin, button2_pin):
        self.button1 = machine.Pin(button1_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button2 = machine.Pin(button2_pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button1.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.button1_pressed)
        self.button2.irq(trigger=machine.Pin.IRQ_FALLING, handler=self.button2_pressed)

    def button1_pressed(self, pin):
        _thread.start_new_thread(run_toilet, ())

    def button2_pressed(self, pin):
        _thread.start_new_thread(run_web, ())

if __name__ == "__main__":
    Buttoner(69,69) # chage