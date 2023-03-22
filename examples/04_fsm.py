from naoqi import ALProxy
import time


IPs = {
	"PABLO_ID" : 	"192.168.0.101",
	"LYRIA_ID" : 	"192.168.0.106" ,
	"KOSHKA_ID" :	"192.168.0.103",
	"ANGELINA_ID" : "192.168.0.102"
}


colors = {	"blue": 0xff ,
			"red": 0xff00, 
			"green": 0xff0000 
		}

def bumpers(proxy):

	left_bumper_val = proxy.getData("LeftBumperPressed")
	right_bumper_val = proxy.getData("RightBumperPressed")

	return left_bumper_val, right_bumper_val


def next_state(l, r, current_state):
	
	if (current_state == 0) & (r >0):
		next_state = 2
	elif (current_state == 0) & (l>0):
		next_state = 1

	elif (current_state == 1) & (r >0):
		next_state = 0
	elif (current_state == 1) & (l >0):
		next_state = 3

	elif (current_state == 2) & (l>0): 
		next_state = 0
	elif (current_state == 2) & (r>0): 
		next_state = 3

	elif (current_state == 3) & (r > 0):
		next_state = 1
	elif (current_state == 3) & (l > 0):
		next_state = 2

	else: 
		next_state = current_state
	

	return next_state 





def turn_ear_on_eye_color_a(led_proxy):
	intensity = 1.0
	duration = 1.0
	color = "blue"
	led_proxy.fade('EarLeds', intensity, duration)
	led_proxy.fadeRGB("FaceLeds",  color, 0.1)

def turn_ear_on_eye_color_b(led_proxy): 
	intensity = 1.0
	duration = 1.0
	color = "red"
	led_proxy.fade('EarLeds', intensity, duration)
	led_proxy.fadeRGB("FaceLeds",  color, 0.1)

def turn_ear_off_eye_color_a(led_proxy):
	intensity = 0
	duration = 1.0
	color = "blue"
	led_proxy.fade('EarLeds', intensity, duration)
	led_proxy.fadeRGB("FaceLeds",  color, 0.1)

def turn_ear_off_eye_color_b(led_proxy):
	intensity = 0
	duration = 1.0
	color = "red"
	led_proxy.fade('EarLeds', intensity, duration)
	led_proxy.fadeRGB("FaceLeds",  color, 0.1)





def main(): 

	memory_proxy = ALProxy("ALMemory", IPs["LYRIA_ID"], 9559)
	led_proxy = ALProxy("ALLeds", IPs["LYRIA_ID"], 9559)
	
	color = 0
	# Reset the colors of the eyes: 
	led_proxy.fadeRGB("FaceLeds", color, 0.1)

	next_state_ = 0
	current_state = 0


	while True:
		l, r = bumpers(proxy = memory_proxy)

		#print("Left Bumper Value" + str(l) + "\n")
		#print("Right Bumper value" + str(r) + "\n")
		print(current_state)

		if current_state == 0:
			turn_ear_on_eye_color_a(led_proxy)
			next_state_ = next_state(l, r, current_state) 

		elif current_state == 1: 
			turn_ear_on_eye_color_b(led_proxy)
			next_state_ = next_state(l, r, current_state)

		elif current_state == 2:
			turn_ear_off_eye_color_a(led_proxy)
			next_state_ = next_state(l, r, current_state)
		elif current_state == 3:
			turn_ear_off_eye_color_b(led_proxy)
			next_state_ = next_state(l, r, current_state)

		current_state = next_state_


	



if __name__ == "__main__": 

	main()