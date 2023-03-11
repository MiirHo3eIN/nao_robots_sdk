# nao_robots_sdk
Useful content to work with NAO V6 robots - Python SDK 


## Getting Started with the SDK


### Step 01: python 2.7 Installation. 

You can either go to [here](https://www.python.org/downloads/release/python-270/) (official website of python) or download it [here](add__the__link). Then, you can simply install the executer (.exe file) for windows and () for Mac.


Hints on Installation: 

1. Make sure that the version of python that you are installing is compatiable with your OS. For instance, if you are using windows 64 bit version, make sure that you are installing python 2.7 - 64 bits.
	
2. Install python for all users of your OS.  

### Step 02: Add(check) for python 2.7 to(in) your variable environment. 

For Windows: 
In your search box type ``` Edit environment variables for your account ``` and press enter.

Look for the "Path" in the "User variables for "your user name>" and double click on it.

If python 2.7 is already existed adjust it to be on top of your list (like image 01)

otherwise, if python 2.7 is not in the list press "New" and add the two path to have a setup like image 01.

![Image 01](docs/image_01.png)


Finally to make sure that you have installed python 2.7, you can run the idle and print("Hello World") 


For Mac: TBA from Luca 

For Linux: just drop [me](amirhossein.moallem2@unibo.it) a message and we can do it together. 

### Step 03: Configuring the Naoqi - SDK 

You can find the packages and libraries of Nao in the following lists: 

Please download SDKs for your OS and unzip them. You can find at aldebaran official web-page or the corresponding  

- [Official Web-page](https://www.aldebaran.com/fr/support/nao-6/downloads-softwares)

Or here:

- [Windows OS - 64](https://drive.google.com/drive/folders/10oGjYZyq_hBb_6_i7BMWUOhsODQLsKqu)

- [Mac OS](https://drive.google.com/drive/folders/1hOIRb9Ys9uM-thReRW-OHCo9aXzhQNBn)

After extracting, give them a proper name, let's say "naoqi_sdk" and copy them in the site-packages of your OS. 
If you did not change the setting during python 2.7 installation, site-packages should be in the following directiosries: 


For windows:

	-  C:\Python27\Lib\site-packages


For MAC: 

	- TBD by Luca


Finally, you will need to add the python sdk to your python environment. To do so, open ``` Edit environment variables for your account ``` as you did in step 02. 

Similar to step 02, in the "User variables for "your user name>" click on New and add the following path as shown in [image 02]: 

![Image 02](docs/image_02.png)



### Step 04: Hello World Test

Now you should be able to run your first python script with the Nao Robot. For that you can navigate to examples and run the hello_world.py   















