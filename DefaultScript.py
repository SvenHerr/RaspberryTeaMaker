import machine
import utime
 

A = 5
B = 6
C = 8
D = 9

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


led_red.value(0)
led_green.value(0)
led_yellow.value(0)
led_blue.value(0)

spule1.value(0)
spule2.value(0)
spule3.value(0)
spule4.value(0)
