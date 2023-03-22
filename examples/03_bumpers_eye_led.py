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


trun_left_eye_on  = lambda led_proxy,color: led_proxy.fadeRGB("LeftFaceLeds",  color, 0.1)
trun_left_eye_off  = lambda led_proxy : led_proxy.fadeRGB("LeftFaceLeds",  0x00, 0.1)
turn_right_eye_on = lambda led_proxy,color: led_proxy.fadeRGB("RightFaceLeds", color, 0.1)
turn_right_eye_off = lambda led_proxy : led_proxy.fadeRGB("RightFaceLeds", 0x00, 0.1)


def main(): 

	memory_proxy = ALProxy("ALMemory", IPs["LYRIA_ID"], 9559)
	
	led_proxy = ALProxy("ALLeds", IPs["LYRIA_ID"], 9559)
	
	color = 0
	# Reset the colors of the eyes: 
	led_proxy.fadeRGB("FaceLeds", color, 0.1)

	while True:
		l, r = bumpers(proxy = memory_proxy)

		print(str(l) + "\n")
		print(str(r) + "\n")


		previous_vals = [0,0]
		current_val = [0,0]



		if l> 0: 
			trun_left_eye_on(led_proxy, colors["blue"])
			time.sleep(0.100)
		if r>0: 
			turn_right_eye_on(led_proxy, colors["red"]) 
	



if __name__ == "__main__": 

	main()