import sys
import time
from naoqi import ALProxy



# It is a global port to connect to the ROBOTs. Do not change it. 
PORT = 9559


# Configuration of the Script 
fractionMaxSpeed_posture_ = 0.8
fractionMaxSpeed_head_ = 0.2


# you can find all the possible angles in this link <http://doc.aldebaran.com/2-8/family/nao_technical/joints_naov6.html>

head_angles_z_axis = [-1.526988, -0.903033, -0.756077, -0.486074, 0.0, 0.486074, 0.756077, 0.903033, 1.526988] # 9 angles

# Z - axis 
#angles = [-1.5,0,1.5]
    
time_list = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 ,9.0]

isAbsolute = True

# Set the Target the headYaw to move around. 
head_joint_name_ = "HeadYaw"
inital_z_angle_ = 0


# Track Motion Configuration ------------------

tracker_target_name_ = "RedBall"

diameter_of_ball_ = 0.15

# mode of tracker in case of finding the ball
tracker_body_mode_ = "Move"
         







class ball_kicker: 

    def __init__(self, robot_IP):
        
        # IP of your robot. 
        self.robot_ip_ = robot_IP
        try:
            # To look for the ball
            self.motion_proxy   = ALProxy("ALMotion", self.robot_ip_, PORT)
            # To Change the Postures of the Robot
            self.posture_proxy = ALProxy("ALRobotPosture", self.robot_ip_, PORT)
            # To track the red ball 
            self.tracker_proxy = ALProxy("ALTracker", self.robot_ip_, PORT)
        except Exception,e:
            print "Could not create proxy to ALProxy"
            print "Error was: ",e
            sys.exit(1)

    def initial_posistion(self):
        
        # Go to posture Stand
        self.posture_proxy.goToPosture("StandInit", fractionMaxSpeed_posture_)
        # Add target to track.
        self.tracker_proxy.registerTarget(tracker_target_name_, diameter_of_ball_)
        # Set the tracker mode
        self.tracker_proxy.setMode(tracker_body_mode_)
        # Start the tracker 
        self.tracker_proxy.track(tracker_target_name_) 
        # Turn Head Joints On. 
        self.motion_proxy.setStiffnesses("Head", 1.0)


    
    
    def final_position(self):
        self.tracker_proxy.stopTracker()
        self.tracker_proxy.unregisterAllTargets()
        self.posture_proxy.goToPosture( "Sit", fractionMaxSpeed_posture_)



    def tracker_lost_status(self): 
       return self.tracker_proxy.isTargetLost()




    def find_ball(self): 
        # Find the ball. Returns the status of the tracker.  

        # Turn Head Joint On
        self.motion_proxy.setStiffnesses("Head", 1.0)
        # Set initial position of the head
        self.motion_proxy.setAngles(head_joint_name_, inital_z_angle_ ,fractionMaxSpeed_head_)
        
        tracking_status_ = self.tracker_lost_status()
        
        for indx, z_angle_ in enumerate(head_angles_z_axis): 
            if tracking_status_:
                # change the angle of head joints
                self.motion_proxy.angleInterpolation(head_joint_name_, z_angle_, time_list[indx], isAbsolute)
                tracking_status_ = self.tracker_lost_status()
            else:
                # Turn Head joints off 
                self.motion_proxy.setStiffnesses("Head", 0.0)
                # The ball is find 
                return tracking_status_ 
        return tracking_status_
    def track_ball(self):

        """
        you can find methods of ALTrack in this link <http://doc.aldebaran.com/2-8/naoqi/trackers/altracker-api.html#ALTrackerProxy>
        """

        # Start the tracker 
        self.tracker_proxy.track(tracker_target_name_)
        tracking_status_ = self.tracker_lost_status()
        return tracking_status_




def main():
    
    robot_IP = "192.168.0.101"
    # Make an object of ball_kicker class. 
    ball_kicker_instance = ball_kicker(robot_IP)
    
    # Get into the inital position
    ball_kicker_instance.initial_posistion()

    # Get the lost status
    tracking_status_ = ball_kicker_instance.tracker_lost_status()

    try: 
        while True:
            if tracking_status_: 
                tracking_status_ = ball_kicker_instance.find_ball() 
            else: 
                tracking_status_ = ball_kicker_instance.track_ball()
            
            print(tracking_status_)
    except KeyboardInterrupt:
        print
        print "Interrupted by user"
        print "Stopping..."

    time.sleep(3.0)

    # Come back to sitting position
    ball_kicker_instance.final_position()



if __name__ == "__main__":
    

    main()


