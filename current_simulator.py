#!/usr/bin/python
import time
import random


try:
       while 1:
           print "_________________________________________"
           c1 = random.random()*3
           c2 = random.random()*5
           c3 = random.random()*3
           print "\nCurrent 1: %s Ampers" % c1
           print "\nCurrent 2: %s Ampers" % c2
           print "\nCurrent 3: %s Ampers" % c3

           P1 = c1*230
           P2 = c2*230
           P3 = c3*230
           print "\nPower 1: %s Watts" % P1
           print "\nPower 2: %s Watts" % P2
           print "\nPower 3: %s Watts" % P3
           time.sleep(5)

except KeyboardInterrupt:
    print "error"
