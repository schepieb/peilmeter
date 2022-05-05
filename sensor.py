import RPi.GPIO as GPIO
import time
import datetime
import mailtje

def dummymeasure():
    return '{"param":45}'

def measure():
    GPIO.setmode(GPIO.BCM)

    TRIG = 23 
    ECHO = 24

    print("Distance Measurement In Progress")
    GPIO.setwarnings(False)
    
    pulse_start=time.time()
    pulse_end=time.time()
    
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    GPIO.cleanup()

    print(distance)
    now = datetime.datetime.now()
    print(now.strftime('%d:%m:%H:%M'))
    csvbestand = open('/home/pi/share/sensor/CSV/peil.csv','a')
    csvbestand.write(now.strftime('%d:%m;%H:%M;'))
    csvbestand.writelines(str(distance) + '\n')

    # return '{"param":' + str(distance) +'}'
    alarmafstand = 10
    if (distance) > alarmafstand:
        print("groter dan " + str(alarmafstand))
        mailtje.stuurbericht()

#while True
measure()
#    sleep()
