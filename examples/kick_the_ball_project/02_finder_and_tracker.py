import sys
import time
from naoqi import ALProxy

# Configuration of the Script 
fractionMaxSpeed_posture = 0.8
fractionMaxSpeed_head = 0.2
#angles = [-2.086017, -1.526988, -1.089958, -0.903033, -0.756077, -0.486074, 
#            0.0, 
#            0.486074, 0.756077, 0.903033, 1.089958, 1.526988, 2.086017]


# Z - axis 
angles = [-1.5,0,1.5]
    
time_list = [2.0,4.0,6.0]

isAbsolute = True


targetName = "RedBall"
diameterOfBall = 0.15
PORT = 9559


def ball_detector(motionProxy, tracker_lost_status): 
    pass

def ball_tracker(): 


    pass 

def tracker_lost_status_computer(tracker_proxy): 
    return tracker_proxy.isTargetLost()

def main(robotIP):
    

    try:
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
        posture_proxy = ALProxy("ALRobotPosture", robotIP, PORT)
        tracker = ALProxy("ALTracker", robotIP, PORT)
    except Exception,e:
        print "Could not create proxy to ALProxy"
        print "Error was: ",e
        sys.exit(1)






    # Go to posture Stand
    posture_proxy.goToPosture("StandInit", fractionMaxSpeed_posture)

    # Turn the Head On. 
    motionProxy.setStiffnesses("Head", 1.0)

    # Add target to track.
    tracker.registerTarget(targetName, diameterOfBall)

    # set mode
    mode = "Move"
    tracker.setMode(mode)

    # Then, start tracker.
    tracker.track(targetName) 

    angle_indx = 0
    # Target the headYaw to move around. 
    names = "HeadYaw"
    angle = angles[0]

    motionProxy.setAngles(names,angle,fractionMaxSpeed_head) 
    # wait half a second
    time.sleep(0.5)
    next_state = 1
    track_losst_status = 0
     
    try: 
        while True:
            track_losst_status = tracker_lost_status_computer(tracker)
            print(track_losst_status)    
            for angle in range(0, len(angles)):
                #print(angle)
                motionProxy.angleInterpolation(names, angles[angle], time_list[angle], isAbsolute)
                #time.sleep(0.5)
                if track_losst_status:
                    motionProxy.setStiffnesses("Head", 1.0)
                    track_losst_status = tracker_lost_status_computer(tracker) 
                    continue
                else: 
                    # Turn off the Head Stiffness.
                    motionProxy.setStiffnesses("Head", 0.0)
                    tracker.track(targetName)

                
    except KeyboardInterrupt:
        print
        print "Interrupted by user"
        print "Stopping..."

    #time.sleep(3.0)


    tracker.stopTracker()
    tracker.unregisterAllTargets()
    posture_proxy.goToPosture( "Sit", fractionMaxSpeed_posture)

if __name__ == "__main__":
    robotIp = "192.168.0.101"

    main(robotIp)


