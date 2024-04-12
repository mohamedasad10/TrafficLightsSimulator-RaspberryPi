import socket
import RPi.GPIO as GPIO
import time

from gpiozero import LED

# Setup GPIO pins for traffic lights
red_pin = 25
yellow_pin = 8
green_pin = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

def change_traffic_light_colors():

    red_led = LED(25)

    yellow_led = LED(8)

    green_led = LED(7)

    def red_light():
        red_led.on()
        yellow_led.off()
        green_led.off()
    
    def yellow_light():
        red_led.off()
        yellow_led.on()
        green_led.off()
    
    def green_light():
        red_led.off()
        yellow_led.off()
        green_led.on()
    
    while True:
        red_light()
        time.sleep(3)
        
        green_light()
        time.sleep(3)
        
        yellow_light()
        time.sleep(1)

def pedestrianCrossing():
    red_led = LED(25)
    yellow_led = LED(8)
    green_led = LED(7)

    def red_light():
        red_led.on()
        yellow_led.off()
        green_led.off()

s = socket.socket()
print('Socket successfully created')
port = 56789
s.bind(('', port))
print(f'Socket binded to port {port}')
s.listen(5)
print('Socket is listening')

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    message = c.recv(1024).decode()
    if message == "Change traffic light colors":
        change_traffic_light_colors()
        response = "Traffic light colors changed"
    else:
        response = "Invalid message"
    c.send(response.encode())
    c.close()