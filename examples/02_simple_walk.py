from naoqi import ALProxy




IPs = {
	"PABLO_ID" : 	"192.168.0.101",
	"LYRIA_ID" : 	"192.168.0.106" ,
	"KOSHKA_ID" :	"192.168.0.103",
	"ANGELINA_ID" : "192.168.0.102"
}



def main():


	motion_proxy = ALProxy("ALMotion", IPs["KOSHKA_ID"], 9559)
	
	#Turn Stiffness ON for 
	motion_proxy.setStiffnesses("Body", 1.0)

	# Initialize the Move
	motion_proxy.moveInit()

	# Destination of the Track
	motion_proxy.moveTo(0.5, 0, 0)




if __name__ == '__main__':
	main()