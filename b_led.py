# For Single - LED blink:
import RPi.GPIO as gp
from time import sleep
gp.setwarnings(False)
gp.setmode ( gp.BOARD)
gp.setup(8, gp.out,initial=gp.Low)
while True:
    gp.output(8,gp.HIGH)
    sleep(1)
    gp.output(8,gp.LOW)
    sleep(1)
# For Multi - LED blink:
import RPi.GPIO as gp
from time import sleep
gp.setwarnings(False)
gp.setmode ( gp.BOARD)
gp.setup(8, gp.out,initial=gp.Low)
gp.setup(16, gp.out,initial=gp.Low)
while True:
    gp.output(8,gp.HIGH)
    gp.output(16,gp.LOW)
    sleep(1)
    gp.output(8,gp.LOW)
    gp.output(16,gp.HIGH)
    sleep(1)