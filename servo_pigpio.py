import pigpio
import time

gpio_pin0 = 12
duty_min = 0.7
duty_max = 2.2
pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)




i = 0.7

while True:

	i = i + 0.2
	if(i > 2.3):
		i = 0.7
	pi.hardware_PWM(gpio_pin0, 50, (i/20.0)*1000000)
	print(str(i))
	print(str(int((i/20.0) * 1000000)))
	time.sleep(1.0)


#	pi.hardware_PWM(gpio_pin0, 50, (duty_max/20.0) * 1000000)
#	print("max", ( duty_max/20.0) * 1000000)
#	time.sleep(1.0)

