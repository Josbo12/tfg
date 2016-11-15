#!/usr/bin/python
import serial
ser = serial.Serial('/dev/ttyAMA0', 38400, timeout=1)
ser.open()

try:
       while 1:
               response = ser.readline()
               z = response.split(",")
               if len(z)>=2:
                       print "Power 1: %s Watts" % z[0]
                       print "Power 2: %s Watts" % z[1]
                       print "Power 3: %s Watts" % z[2][:-2]
except KeyboardInterrupt:
       ser.close()
