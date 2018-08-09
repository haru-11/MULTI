import time
import pigpio

pin_sb = 22
in1 = 27
in2 = 17

tf = True

pi = pigpio.pi()

pi.set_mode(pin_sb, pigpio.OUTPUT)
pi.set_mode(in1, pigpio.OUTPUT)
pi.set_mode(in2, pigpio.OUTPUT)

pi.set_PWM_frequency(pin_sb, 800)
pi.set_PWM_range(pin_sb, 255)

pi.write(in1, 1)
pi.write(in2, 0)
try:

	while True:
		pi.set_PWM_dutycycle(pin_sb, 255)
except KeyboardInterrupt:
	pi.set_PWM_dutycycle(pin_sb, 0)
	pi.write(in1, 1)
	pi.write(in2, 0)
