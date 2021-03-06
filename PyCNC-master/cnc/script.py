# This version uses new-style automatic setup/destroy/mapping
# Need to change /etc/webiopi

# Imports
import os
import webiopi
import sys,time
import readline
import atexit

sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master')
sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master/cnc/hal_raspberry')

import cnc.logging_config as logging_config
from cnc.gcode import GCode, GCodeException
from cnc.gmachine import GMachine, GMachineException



# Enable debug output
webiopi.setDebug()



# Interpreter Version
print('Python Interpreter Version:', sys.version)
print()

machine = GMachine()

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# -------------------------------------------------- #
# Constants definition                               #
# -------------------------------------------------- #
LED_GREEN   = 25

STEPPER_STEP_PIN_X  = 13
STEPPER_DIR_PIN_X   = 6
ENDSTOP_PIN_X       = 24

STEPPER_STEP_PIN_Y  = 21
STEPPER_DIR_PIN_Y   = 20
ENDSTOP_PIN_Y       = 23

STEPPER_STEP_PIN_Z  = 26
STEPPER_DIR_PIN_Z   = 19
ENDSTOP_PIN_Z       = 17



# -------------------------------------------------- #
# Convenient PWM Function                            #
# -------------------------------------------------- #
# Set the speed of two motors
# def set_speed(speed):
#     GPIO.pulseRatio(LS, speed)
#     GPIO.pulseRatio(RS, speed)


# -------------------------------------------------- #
# Blink Functions                                    #
# -------------------------------------------------- #
def blink_1():
    GPIO.output(LED_GREEN, GPIO.HIGH)
    webiopi.sleep(0.2)
    GPIO.output(LED_GREEN, GPIO.LOW)
    webiopi.sleep(0.1)

def blink_2():
    blink_1()
    blink_1()

def blink_3():
    blink_1()
    blink_1()
    blink_1()


# Called by WebIOPi at script loading
def setup():
    webiopi.debug("Basic script - Setup")
    # Setup GPIOs
    GPIO.setFunction(LED_GREEN, GPIO.OUT)
    GPIO.digitalWrite(LED_GREEN, GPIO.LOW)

    webiopi.debug("Set Green LED as ON OFF")

    # # # X Axis
    # GPIO.setFunction(STEPPER_STEP_PIN_X, GPIO.OUT)
    # GPIO.setFunction(STEPPER_DIR_PIN_X, GPIO.OUT)
    # GPIO.setFunction(ENDSTOP_PIN_X, GPIO.IN)
    # #
    # # # Y Axis
    # GPIO.setFunction(STEPPER_STEP_PIN_Y, GPIO.OUT)
    # GPIO.setFunction(STEPPER_DIR_PIN_Y, GPIO.OUT)
    # GPIO.setFunction(ENDSTOP_PIN_Y, GPIO.IN)
    # #
    # # # Z Axis
    # GPIO.setFunction(STEPPER_STEP_PIN_Z, GPIO.OUT)
    # GPIO.setFunction(STEPPER_DIR_PIN_Z, GPIO.OUT)
    # GPIO.setFunction(ENDSTOP_PIN_Z, GPIO.IN)

    logging_config.debug_disable()

    do_line("x5.0 y5.0 z5.0")
    do_line("x0.0 y0.0 z0.0")
    print("Tested XYZ Motion +5mm and Back")


    # GPIO.setFunction(LED_GREEN, GPIO.PWM)
    # GPIO.pwmWrite(LED_GREEN, 0.5)  # set to 50% ratio



# Looped by WebIOPi
# def loop():
#
#     webiopi.debug("Loop")
#     # Toggle LED each 1 second
#     value = not GPIO.digitalRead(LED_GREEN)
#     GPIO.digitalWrite(LED_GREEN, value)
#     webiopi.sleep(1)




# Called by WebIOPi at server shutdown
def destroy():
    # webiopi.debug("Basic script - Destroy")
    # Reset GPIO functions
    # GPIO.setFunction(STEPPER_STEP_PIN_X, GPIO.IN)
    # GPIO.setFunction(STEPPER_DIR_PIN_X, GPIO.IN)
    # GPIO.setFunction(STEPPER_STEP_PIN_Y, GPIO.IN)
    # GPIO.setFunction(STEPPER_DIR_PIN_Y, GPIO.IN)
    # GPIO.setFunction(STEPPER_STEP_PIN_Z, GPIO.IN)
    # GPIO.setFunction(STEPPER_DIR_PIN_Z, GPIO.IN)
    # GPIO.setFunction(LED_GREEN, GPIO.IN)

    machine.release()





# -------------------------------------------------- #
# Macro definition part                              #
# -------------------------------------------------- #
@webiopi.macro
def go_1():
    blink_1()
    do_line("z0.0")


@webiopi.macro
def go_2():
    blink_2()
    do_line("z10.0")

@webiopi.macro
def go_3():
    blink_3()
    do_line("z20.0")

@webiopi.macro
def pwmMode():
    GPIO.setFunction(LED_GREEN, GPIO.PWM)
    GPIO.pwmWrite(LED_GREEN, 0.5)  # set to 50% ratio
    webiopi.debug("Set Green LED as PWM")

@webiopi.macro
def onoffMode():
    GPIO.setFunction(LED_GREEN, GPIO.OUT)
    GPIO.digitalWrite(LED_GREEN, GPIO.LOW)
    webiopi.debug("Set Green LED as ON OFF")

@webiopi.macro
def myMacroWithArgs(args):
    for n in range(0, int(args)):
        blink_1()

@webiopi.macro
def send_gcode(line):
    line = line.replace("%20", " ")
    # webiopi.debug("Process - " + line)
    result = do_line(line)
    str=""
    if  result != True:
        str = result
    t = time.strftime("%H:%M:%S", time.gmtime())
    return "[" + t + "]: " + line + " >>> "+ str





def do_line(line):
    try:
        g = GCode.parse_line(line)
        res = machine.do_command(g)
    except (GCodeException, GMachineException) as e:
        return 'ERROR ' + str(e)
    if res is not None:
        return 'OK ' + res
    else:
        return 'OK'
    return True


