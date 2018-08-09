import pigpio
import time

pi = pigpio.pi()

class MCP3002:

	def __init__(self):
		pi = pigpio.pi()
		self.h = pi.spi_open(0, 75000, 0)

	def get_ADC(self):
		c, d =pi.spi_xfer(self.h,[0x68,0x00])
		return (d[0]<<8)+d[1]


adc =  MCP3002()

try:

	while True:
		d = adc.get_ADC()
		time.sleep(1.0)
		print(str(d))

except KeyboardInterrupt:
	pass
