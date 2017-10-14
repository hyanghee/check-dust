#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

import sys
import serial, time,struct
import random
import datetime
import  Adafruit_DHT
import urllib2
#import  urllib.request  #python3 thingspeak

thingurl_t ="https://api.thingspeak.com/update?api_key=JYQPWHB0ENBYQ3TP&field2="
HUM ="&field4="

GPIO_TEM = 2
time_s = random.randrange(60,100)

def read_dht():
    # Parse command line parameters.
    sensor = Adafruit_DHT.DHT11
    pin = GPIO_TEM
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        return temperature, humidity
    else:
        print('Failed to get reading. Try again!')
        return 0

def main():
   print "starting ....."
   while True:
      try: 
        temp, hum = read_dht()
        urlt = thingurl_t + str(temp) + HUM + str(hum)
#temp / hum
        f =  urllib2.urlopen(urlt)
        data = str(f.read())
        print("Got temp ", data)
        print(urlt)
        break
#        time.sleep(time_s)

      except:
        print "exiting..." 
        break

if __name__ == '__main__':
     main()


### MAIN  

#temp, hum = read_dht()
#if temp is not None:
#     print "test  " , temp,   "test2 ",  hum
#     print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum))
#     print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temp, hum))
