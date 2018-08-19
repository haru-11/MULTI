
#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import serial
import time
import pigpio

time.sleep(1.0)

pi = pigpio.pi()
pi.set_mode(6,pigpio.OUTPUT)
pi.set_mode(5,pigpio.OUTPUT)
pi.write(6,0)
time.sleep(1)
pi.write(5,0)
time.sleep(1)
pi.write(5,1)

s = serial.Serial('/dev/serial0', 115200)

try:
	i = 10
	while i>0:
		s.write( "for sleep"+str(i)+"sec\r\n" )
		print("for sleep"+str(i)+"sec\r\n")
		i = i - 1
		time.sleep(1.0)
	pi.write(6,1)
	while True:
		s.write("return"+str(i)+"\r\n")
		print("return"+str(i)+"\r\n")
		time.sleep(1.0)
		i = i + 1
		if i== 10:
			s.write(6,0)
except KeyboardInterrupt:
	s.close()
