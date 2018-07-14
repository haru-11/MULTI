
import time
import pigpio

pin_sb = 17
gpio_pin0 = 13
in1 = 27
in2 = 22
o_s = 18
o_b = 23
o_r = 24
o_l = 25
led1 = 0
led2 = 5
led3 = 6

tf = True

pi = pigpio.pi()
pi.set_mode(gpio_pin0, pigpio.OUTPUT)

pi.set_mode(pin_sb, pigpio.OUTPUT)
pi.set_mode(in1, pigpio.OUTPUT)
pi.set_mode(in2, pigpio.OUTPUT)
pi.set_mode(o_s, pigpio.INPUT)
pi.set_mode(o_b, pigpio.INPUT)
pi.set_mode(o_r, pigpio.INPUT)
pi.set_mode(o_l, pigpio.INPUT)
pi.set_mode(led1, pigpio.OUTPUT)
pi.set_mode(led2, pigpio.OUTPUT)
pi.set_mode(led3, pigpio.OUTPUT)

pi.set_PWM_frequency(pin_sb, 800)
pi.set_PWM_range(pin_sb, 255)
pi.set_PWM_dutycycle(pin_sb, 0)

pi.hardware_PWM(gpio_pin0, 50,( 0.15/20.0) * 1000000)

pi.write(in1, 0)
pi.write(in2, 0)
pi.write(led1, 1)
time.sleep(0.5)
pi.write(led1, 0)
time.sleep(0.5)
pi.write(led1, 1)

while True:
	
	tf = True

	pi.set_PWM_dutycycle(pin_sb, 0)
	pi.hardware_PWM(gpio_pin0, 50,( 0.15/20.0) * 1000000)
	pi.write(led2, 0)
	pi.write(led3, 0)
	
	while ( pi.read( o_s ) == 1 ):
		if( tf == True) :
			pi.write(in1, 0)
			pi.write(in2,1)

			pi.write(led2, 1)

			#pi.set_PWM_dutycycle(pin_sb, 50)
			#time.sleep(1)
			#pi.set_PWM_dutycycle(pin_sb, 100)
		#	time.sleep(1)
		#	pi.set_PWM_dutycycle(pin_sb, 150)
		#	time.sleep(1)
		#	pi.set_PWM_dutycycle(pin_sb, 200)

			tf = False
		else:
			pi.set_PWM_dutycycle(pin_sb, 255)
		        while ( pi.read( o_r ) == 1 ):

	                        pi.hardware_PWM(gpio_pin0, 50,( 1.0/20.0) * 1000000)

	                	pi.write(led3, 1)

        		pi.hardware_PWM(gpio_pin0, 50,( 1.5/20.0) * 1000000)
        		pi.write(led3, 0)
        		while ( pi.read( o_b ) == 1 ):

                        	pi.hardware_PWM(gpio_pin0, 50,( 2.0/20.0) * 100000)

				pi.write(led3, 1)

        		pi.hardware_PWM(gpio_pin0, 50,( 1.5/20.0) * 1000000)
        		pi.write(led3, 0)

	pi.write(in1, 0)
	pi.write(in2,0)
	pi.write(led2, 0)

        while ( pi.read( o_b ) == 1 ):
                if( tf == True) :
                        pi.write(in1, 1)
                        pi.write(in2, 0)

                       # pi.set_PWM_dutycycle(pin_sb, 50)
                       # time.sleep(1)
                       # pi.set_PWM_dutycycle(pin_sb, 100)
                       # time.sleep(1)
                       # pi.set_PWM_dutycycle(pin_sb, 150)
                       # time.sleep(1)
                       # pi.set_PWM_dutycycle(pin_sb, 200)

                        tf = False
                else:
                        pi.set_PWM_dutycycle(pin_sb, 255)
			pi.write(led2, 1)
                        while ( pi.read( o_r ) == 1 ):

                                pi.hardware_PWM(gpio_pin0, 50,( 1.0/20.0) * 1000000)

                                pi.write(led3, 1)

                        pi.hardware_PWM(gpio_pin0, 50,( 1.5/20.0) * 1000000)
                        pi.write(led3, 0)
                        while ( pi.read( o_l ) == 1 ):

                                pi.hardware_PWM(gpio_pin0, 50,( 2.0/20.0) * 1000000)

                                pi.write(led3, 1)

                        pi.hardware_PWM(gpio_pin0, 50,( 1.5/20.0) * 1000000)
                        pi.write(led3, 0)
        pi.write(in1, 0)
        pi.write(in2, 0)
        pi.write(led2, 0)

        while ( pi.read( o_r ) == 1 ):
                if( tf == True):
			pi.hardware_PWM(gpio_pin0, 50,( 1.0/20.0) * 1000000)


			tf = False
		else:
			pi.write(led3, 1)

	pi.hardware_PWM(gpio_pin0, 50,( 1.5/20.0) * 1000000)
	pi.write(led3, 0)
        while ( pi.read( o_l ) == 1 ):
                if( tf == True) :
                        pi.hardware_PWM(gpio_pin0, 50,( 2.0/20.0) * 1000000)


                        tf = False
                else:
                        pi.write(led3, 1)

        pi.hardware_PWM(gpio_pin0, 50,( 1.5/20.0) * 1000000)
        pi.write(led3, 0)

