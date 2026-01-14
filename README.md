# Circuit Breakers: Line Following Robot – Webots Simulation

## Overview
This project demonstrates a simple line-following robot simulated using **Webots** and programmed in **Python**.  
The built-in **e-puck** robot is used to detect and follow a thin black line on a light surface by adjusting its wheel speeds based on ground sensor readings.
The main goal of the project is to achieve smooth and stable line following with minimal oscillation.

---

## Simulation Demonstration Video
🔗 **Simulation Video:**  
https://youtu.be/8G4QwCFs5jI

The video shows the line follower going around the course, with no oscillations and smooth line turning.

---

## Robot and Sensor Configuration
The simulation uses the default **e-puck robot model provided by Webots, along with ground sensors equipped.**

The robot is equipped with **three downward-facing ground sensors**:
- Left ground sensor 
- Center ground sensor  
- Right ground sensor  

These sensors measure the amount of reflected light from the surface below:
- Black surfaces reflect less light and produce lower sensor values  
- White surfaces reflect more light and produce higher sensor values  
A threshold value is used to differentiate between the black line and the background.  

---

## Working Principle (Step-by-Step)
### 1. Line Detection

At every simulation step, the robot reads values from all three ground sensors.  
By comparing these values with a threshold, the robot determines whether each sensor is currently over the line or the background.

---

### 2. Processing Sensor Data
To estimate the position of the line relative to the robot, each sensor is assigned a positional weight:
- Left sensor gives a negative value  
- Center sensor → zero  
- Right sensor gives a positive value  

The sensor readings are combined using a weighted average to calculate where the line lies under the robot.  
This approach provides smooth feedback instead of random left/right turning.

---

### 3. Motor Speed Control
The e-puck robot uses **differential drive**, meaning each wheel can be controlled independently.

- A base speed is applied to both motors.
- Based on the calculated line position, a steering correction is generated.
- One motor slows down while the other speeds up, causing the robot to turn.

This continuous adjustment keeps the robot centered on the line.

---

## Control Logic

### Moving Forward
- When the center sensor detects the line and the other sensors detect the background, the robot is aligned correctly.
- Both motors run at the same speed.
- The robot moves straight along the line.

---

### Turning Left
- When the line is detected more strongly on the left side, the robot has drifted right.
- The left motor slows down while the right motor maintains its speed.
- The robot turns left to return to the center of the line.

---

### Turning Right
- When the line is detected more strongly on the right side, the robot has drifted left.
- The right motor slows down while the left motor maintains its speed.
- The robot turns right to re-center itself.

---

### Line Lost Handling
- If none of the sensors detect the line, the robot slows down and continues moving straight.

---

## Enhancements Made
- Used weighted averages for smoother steering  
- Reduced oscillations by avoiding random left/right turns, only following the line   

---

## Known Limitations
- Requires proper threshold tuning for different surfaces  
- Very sharp curves may require a lower base speed  
- Assumes a dark line on a light background  
- No obstacle detection is implemented
- Only uses built-in Webots components

---

## Files Included
- `worlds/` – Webots world (.wbt) file  
- `controllers/` – Python controller code  
- `README.md` – Project documentation  

---

## Notes
The project uses the default e-puck robot model provided by Webots.  
Ground sensors were enabled using official extension slots without modifying the robot’s structure or PROTO files.
