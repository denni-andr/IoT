import RPi.GPIO as gp
gp.Setmode ( gp.BOARD)
gp.setup(8, gPIN)
gp.setup (36, gp.out, initial=gp.Low)
gp.setup (32, gp.out, initial=gp.Low)
while True:
    try:
        print(not gp.input(8))
        gp.output(36,gp.input(8))
        gp.output(32,not gp.input(8))
    except:
        gp.cleanup()