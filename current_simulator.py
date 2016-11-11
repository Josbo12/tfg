#!/usr/bin/python

from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import datetime
import random
import time

USER = 'root'
PASSWORD = 'root'
DBNAME = 'powerdb'


def main():

    host ='localhost'
    port = 8086
    metric = "powerdata"
    series = []


    while True:
           print "_________________________________________"
           now = datetime.datetime.today()
           hostName = "server-%d" % random.randint(1, 5)
           c1 = random.random()*3
           #c2 = random.random()*5
           #c3 = random.random()*3
           #print "\nCurrent 1: %s Ampers" % c1
           #print "\nCurrent 2: %s Ampers" % c2
           #print "\nCurrent 3: %s Ampers" % c3

           P1 = c1*230
           #P2 = c2*230
           #P3 = c3*230
           print "\nPower 1: %s Watts" % P1
           print "Time: %s" %now
           #print "\nPower 2: %s Watts" % P2
           #print "\nPower 3: %s Watts" % P3

           pointValues = {
                   "time": now.strftime ("%Y-%m-%d %H:%M:%S"),
                   # "time": int(past_date.strftime('%s')),
                   "measurement": metric,
                   'fields':  {
                       'value': P1,
                   },
                   'tags': {
                       "hostName": hostName,
                   },
               }
           series.append(pointValues)
           print(series)

           client = InfluxDBClient(host, port, USER, PASSWORD, DBNAME)

           retention_policy = 'awesome_policy'
           client.create_retention_policy(retention_policy, '3d', 3, default=True)


           client.write_points(series, retention_policy=retention_policy)

           time.sleep(10)

if __name__ == '__main__':
    main()
