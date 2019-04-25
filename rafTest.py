#
# Directly Plug Keyboard In RaspberryPi 
# and control with "aswd" (spacebar to stop)
#
# Simple tester for the Roomba Interface
# from create.py
#
# Adjust your ROOMBA_PORT if necessary.
# python game.py 
# starts a pygame window from which the 
# Roomba can be controlled with w/a/s/d.
# Use this file to play with the sensors.
import os, sys
import create
import time
import keyboard
import curses

# Change the roomba port to whatever is on your
# machine. On a Mac it's something like this.
# On Linux it's usually tty.USB0 and on Win
# its to serial port.
ROOMBA_PORT = "/dev/ttyUSB0"

robot = create.Create(ROOMBA_PORT, BAUD_RATE=115200)
robot.toSafeMode()

# pygame.init()

FWD_CMPS = 20 # forward speed in cm per second
ROT_CMPS = 60 # rotation speed in cm per second

# Initialize robot's direction and rotation
robot_dir = 0;
robot_rot = 0;
multiplier = 0;

def update_roomba_dir(robot_dir, delta):
    robot_dir += delta;
    robot.go(robot_dir * FWD_CMPS, 0)
    time.sleep(0.1) # unsure if this is needed
    robot_dir = 0;

def update_roomba_rot(robot_rot, delta): 
    robot_rot += delta;
    robot.go(0, robot_rot * ROT_CMPS)
    time.sleep(0.1) #unsure if this is needed
    robot_rot = 0; 

def move_roomba(multiplier, robot_dir, robot_rot):
     robot.go(FWD_CMPS * robot_dir * multiplier, ROT_CMPS * robot_rot * multiplier)
     time.sleep(0.1)
     

def main():
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)

	robot.resetPose()
        robot_dir = 0;
        robot_rot = 0;
        multiplier = 1.0;
	# px, py, th = robot.getPose()

	while True:
            input = screen.getch()
            if input == ' ':
	        robot_dir = 0;
                robot_rot = 0;
                multiplier = 1.0;
            elif input == ord('r') and multiplier <= 3.0:
                multiplier += 0.1;
            elif input == ord('f') and multiplier > 0.3:
                multiplier -= 0.1;
	    elif input == ord('w'):
		robot_dir = 1;
	    elif input == ord('s'):
		robot_dir = -1;
	    elif input == ord('a'):
		robot_rot = 1;
	    elif input == ord('d'):
		robot_rot = -1;
            else:
                robot_dir = 0;
                robot_rot = 0;

            move_roomba(multiplier, robot_dir, robot_rot);
            curses.flushinp();

if __name__ == '__main__': 
    try:    
        main()
    except Exception as err:
	print (err)
    
    robot.go(0,0)
    robot.close()
    curses.nocbreak();
    curses.echo();
    curses.endwin();
