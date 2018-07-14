import pigpio
import time

pi = pigpio.pi()

h = pi.spi_open(0, 75000, 0)

while True:

	c, d =pi.spi_xfer(h,[0x68,0x00])

	print str((d[0]<<8)+d[1])
	time.sleep(1)
