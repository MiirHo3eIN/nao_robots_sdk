import naoqi 
from naoqi import ALProxy

IPs = {
	"PABLO_ID" : 	"192.168.0.101",
	"LYRIA_ID" : 	"192.168.0.106" ,
	"KOSHKA_ID" :	"192.168.0.103",
	"ANGELINA_ID" : "192.168.0.102"
}



def main(): 

	# Make the proxy to the Memory Class 
	mem_proxy = ALProxy("ALMemory", IPs["ANGELINA_ID"], 9559)

	# Print data list name
	data_list_names = mem_proxy.getDataListName()
	for keys in data_list_names:
		print(keys)
		print("\n")


	# Let's get the data of 
	print("Test Successful!")



if __name__ == "__main__": 


	main()