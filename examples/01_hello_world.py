import naoqi 
from naoqi import ALProxy

IPs = {
	"PABLO_ID" : 	"192.168.0.101",
	"LYRIA_ID" : 	"192.168.0.106" ,
	"KOSHKA_ID" :	"192.168.0.103",
	"ANGELINA_ID" : "192.168.0.102"
}



def main():

	# Make an object of the class you want to use and connecto to the robot you want.

	# Select your robots ID from the IPs table 
	ttx = ALProxy("ALTextToSpeech", IPs["KOSHKA_ID"], 9559)
	
	# Use method say to run the program
	ttx.say("Hello All. Let's play football.")

	print("test successful!")

if __name__ == "__main__":

	# Call the Main function. 
	main()