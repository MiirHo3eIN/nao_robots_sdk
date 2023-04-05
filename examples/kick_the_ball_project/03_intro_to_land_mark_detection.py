import sys
import time
from naoqi import ALProxy



# It is a global port to connect to the ROBOTs. Do not change it. 
PORT = 9559


fractionMaxSpeed_posture_ = 0.8



def main():
    
    robot_IP = "192.168.0.101"
    land_mark_val_name = "LandmarkDetected"
    try: 
        # Make a proxy of the Land Mark Detection 
        mark_detection_proxy = ALProxy("ALLandMarkDetection", robot_IP, PORT)
        # Make a proxy of the Memory to read the result of the LandMark
        memory_proxy = ALProxy("ALMemory", robot_IP, PORT)
        # Make a proxy for the Robot Position 
        posture_proxy = ALProxy("ALRobotPosture", robot_IP, PORT)

    except Exception,e:
        print "Could not create proxy to ALProxy"
        print "Error was: ",e
        sys.exit(1)




    # Stand the robot... 
    posture_proxy.goToPosture("StandInit", fractionMaxSpeed_posture_)

    # Subscribe to the ALLandMarkDetection proxy
    # This means that the module will write in ALMemory with
    
    # period is in ms
    period_land_mark_capture_ = 100
    mark_detection_proxy.subscribe("Test_LandMark", period_land_mark_capture_, 0.0 )

    land_mark_values = []
    try: 
        while True:
            time.sleep(0.1)
            land_mark_values = memory_proxy.getData(land_mark_val_name, 0)
            #print(land_mark_values)
            if land_mark_values != None or land_mark_values != []:   
                if len(land_mark_values) >2 :
                    land_mark_info = land_mark_values[1] 
                    # land_mark_extra_info 
                    print "Mark ID \t %d" %(land_mark_info[0][1][0])
            else: 
                print "No Mark is detected!"

    except KeyboardInterrupt:
        print
        print "Interrupted by user"
        print "Stopping..."

    time.sleep(3.0)

    # Unsubscribe from the module.
    mark_detection_proxy.unsubscribe("Test_LandMark")
    # Come back to sitting position
    posture_proxy.goToPosture("Sit", fractionMaxSpeed_posture_)

    print "Mark Detection is over"
    print "Test Successful!"

if __name__ == "__main__":
    

    main()


