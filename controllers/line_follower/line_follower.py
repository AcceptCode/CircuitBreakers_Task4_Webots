from controller import Robot # module that controls all robot functions

robot = Robot() # defining the robot object
timestep = int(robot.getBasicTimeStep()) # defining a timestep, basically almost ever frame when the simualation is running :)

# Get ground sensors (gs = ground sensor)
gs = []
for i in range(3):
    # gets devices attached to robot
    s = robot.getDevice(f"gs{i}")
    s.enable(timestep)
    gs.append(s)

# Motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

BASE_SPEED = 3.0
MAX_SPEED = 6.28
THRESHOLD = 480

# gs0 - center / gs1 - left / gs2 - right
weights = [-1.0, 0.0, 1.0]  # LEFT, CENTER, RIGHT

while robot.step(timestep) != -1:
    # getting sensor readings from all sensors
    left_val   = gs[2].getValue()
    center_val = gs[1].getValue()
    right_val  = gs[0].getValue()

    values = [left_val, center_val, right_val]

    # Converting to line strength, using raw sensor values
    black = [max(0.0, THRESHOLD - v) for v in values]
    total = sum(black) # sum of all strength readings
    
    # case if line is not found
    if total == 0:
        # moves straight to attempt line finding
        left_motor.setVelocity(0.7 * BASE_SPEED)
        right_motor.setVelocity(0.7 * BASE_SPEED)
        continue
    # computes weighted average of sensor reading relative to position
    # in this case, the colour black contributes more
    position = sum(b * w for b, w in zip(black, weights)) / total
    
    # turns line value to steering value
    steer = position * 1.0
    
    # decreases and increases steer for both left and right simultaneously
    # thus, makiing sure its centered on the black line
    left_speed = BASE_SPEED - steer
    right_speed = BASE_SPEED + steer
    
    # code clamps down on speed, preventing jitter
    left_speed = max(0.0, min(MAX_SPEED, left_speed))
    right_speed = max(0.0, min(MAX_SPEED, right_speed))
    
    # sets maximum velocity
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
    
   # code is done!
   # every frame, the program collects sensor data from the 
   # 3 data sensorts located at the bottom of the e - puck
   # the raw data changes depending on colour
   # it would be less for black, and more for white
   # a weighted average is taken, and black contributes more
   # weighted average is taken to prevent noise, so that the robot does not drive erratically
   # if the reading passes threshold, motor speed and rotation are changed to keep the robot
   # on the center as much as possible.
   
# Team Circuit Breakers