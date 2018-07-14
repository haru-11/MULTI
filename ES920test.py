import serial
import time
s = serial.Serial('/dev/serial0', 115200)

try:
	i = 0
	while True:
		i = i +1
		s.write( "Hello ARLISS_"+str(i)+"\r\n" )
		time.sleep(1.0)

except KeyboardInterrupt:
	s.close()
