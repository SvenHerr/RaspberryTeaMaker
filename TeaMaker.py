import machine
import utime
 

A = 18
B = 19
C = 20
D = 21

LedRed = 1
LedGreen = 3
LedYellow = 2
LedBlue = 0

led_red = machine.Pin(LedRed, machine.Pin.OUT)
led_green = machine.Pin(LedGreen, machine.Pin.OUT)
led_yellow = machine.Pin(LedYellow, machine.Pin.OUT)
led_blue = machine.Pin(LedBlue, machine.Pin.OUT)

spule1 = machine.Pin(A, machine.Pin.OUT)
spule2 = machine.Pin(B, machine.Pin.OUT)
spule3 = machine.Pin(C, machine.Pin.OUT)
spule4 = machine.Pin(D, machine.Pin.OUT)

button_start = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_letgo = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)


def GPIO_SETUP(a,b,c,d):
 spule1.value(a)
 spule2.value(b)
 spule3.value(c)
 spule4.value(d)
 utime.sleep(0.001)

def RIGHT_TURN(deg):

 full_circle = 510.0
 degree = full_circle/360*deg
 GPIO_SETUP(0,0,0,0)

 while degree > 0.0:
  GPIO_SETUP(1,0,0,0)
  GPIO_SETUP(1,1,0,0)
  GPIO_SETUP(0,1,0,0)
  GPIO_SETUP(0,1,1,0)
  GPIO_SETUP(0,0,1,0)
  GPIO_SETUP(0,0,1,1)
  GPIO_SETUP(0,0,0,1)
  GPIO_SETUP(1,0,0,1)
  degree -= 1

def LEFT_TURN(deg):

 full_circle = 510.0
 degree = full_circle/360*deg
 GPIO_SETUP(0,0,0,0)

 while degree > 0.0:
  GPIO_SETUP(1,0,0,1)
  GPIO_SETUP(0,0,0,1)
  GPIO_SETUP(0,0,1,1)
  GPIO_SETUP(0,0,1,0)
  GPIO_SETUP(0,1,1,0)
  GPIO_SETUP(0,1,0,0)
  GPIO_SETUP(1,1,0,0)
  GPIO_SETUP(1,0,0,0)
  degree -= 1

def redLedOn():
 led_red.value(1)

def redLedOff():
 led_red.value(0)

def yellowLedOn():
 led_yellow.value(1)

def yellowLedOff():
 led_yellow.value(0)

def greenLedOn():
 led_green.value(1)

def greenLedOff():
 led_green.value(0)

def default():
 redLedOff()
 yellowLedOff()
 greenLedOff()

def stur():
 yellowLedOn()
 RIGHT_TURN(450)
 LEFT_TURN(450)
 yellowLedOff()
 
def start():
 redLedOn()
 print("bin am start")
 utime.sleep(120)
 stur()
 print("Stur 1")
 utime.sleep(120)
 stur()
 print("Stur 2")
 utime.sleep(120)
 redLedOff()
 greenLedOn()

 RIGHT_TURN(90)
 #LEFT_TURN(90)
 RIGHT_TURN(1550)
 GPIO_SETUP(0,0,0,0)
 
def letgo():
 LEFT_TURN(90)
 #LEFT_TURN(90)
 LEFT_TURN(1550)
 GPIO_SETUP(0,0,0,0)
 greenLedOff()

while True:
 led_blue.value(1)
 if button_start.value() == 1:
        start()
        
 if button_letgo.value() == 1:
        letgo()

 utime.sleep(0.25)



