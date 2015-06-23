# Import libraries for Raspberry Pi GPIO
import RPi.GPIO as GPIO
import time

# Setup pin names by board layut
GPIO.setmode(GPIO.BOARD)
# Assign Solenoid pins as outputs
GPIO.setup(40,GPIO.OUT) # Solenoid 1
GPIO.setup(38,GPIO.OUT) # Solenoid 2
GPIO.setup(37,GPIO.OUT) # Solenoid 3
GPIO.setup(36,GPIO.OUT) # Solenoid 4
GPIO.setup(35,GPIO.OUT) # Solenoid 5
GPIO.setup(33,GPIO.OUT) # Solenoid 6
GPIO.setup(32,GPIO.OUT) # Solenoid 7
GPIO.setup(31,GPIO.OUT) # Solenoid 8
GPIO.setup(29,GPIO.OUT) # Solenoid 9
GPIO.setup(15,GPIO.OUT) # Solenoid 10
GPIO.setup(13,GPIO.OUT) # Solenoid 11
GPIO.setup(12,GPIO.OUT) # solenoid 12

print("TRIACS will be turned on in 5s")
time.sleep(5)
print("TRAICS on")
#GPIO.output(32,True)
GPIO.output(29,True)
#GPIO.output(31,True)
#GPIO.output(15,True)
time.sleep(60)

print("TRIACS OFF")
#GPIO.output(32,False)
GPIO.output(29,False)
#GPIO.output(31,False)
#GPIO.output(15,False)
print("End of script")
