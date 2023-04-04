import time
import argparse
from naoqi import ALProxy

def main(IP_, ball_dimension):
    IP = IP_
    PORT = 9559
    print "Connecting to", IP, "with port", PORT
    #motion = ALProxy("ALMotion", IP, PORT)
    posture = ALProxy("ALRobotPosture", IP, PORT)
    tracker = ALProxy("ALTracker", IP, PORT)


    fractionMaxSpeed = 0.8
    # Go to posture stand
    posture.goToPosture("StandInit", fractionMaxSpeed)

    # Add target to track.
    targetName = "RedBall"
    diameterOfBall = ball_dimension
    tracker.registerTarget(targetName, diameterOfBall)

    # set mode
    mode = "Move"
    tracker.setMode(mode)

    # Then, start tracker.
    tracker.track(targetName)

    print "ALTracker successfully started, now show a red ball to robot!"
    print "Use Ctrl+c to stop this script."

    try:
        while True:
            print(tracker.getTargetPosition())
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user"
        print "Stopping..."

    # Stop tracker, go to posture Sit.
    tracker.stopTracker()
    tracker.unregisterAllTargets()
    posture.goToPosture("Sit", fractionMaxSpeed)
    #motion.rest()

    print "ALTracker stopped."


if __name__ == "__main__" :

    IP = "192.168.0.102"
    ball_dimension = 0.15
    main(IP, ball_dimension)