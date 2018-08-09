import MCP3002_test

adc = MCP3002_test.MCP3002()

while True

	d = adc.get_ADC()
	print str(d)

