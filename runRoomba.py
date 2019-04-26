# Adjust your ROOMBA_PORT if necessary.
# Instructions: 
#   Hit `w` to move the roomba forward
#   Hit `s` to move the roomba backward
#   Hit `a` to rotate the roomba counterclockwise ~90 degrees
#   Hit `d` to rotate the roomba clockwise ~90 degrees
#   Hit `q` to rotate the roomba counterclockwise ~45 degrees
#   Hit `e` to rotate the roomba clockwise ~45 degrees
#   Hit `[spacebar]` to quit application
# Notes:
#   Refrain from holding down buttons as each button logged 
#       will result in the corresponding action (unable to be stopped)
#   If spacebar is not hit to quit, the terminal is still functional
#       but may have formatting issues because the console screen initialized
#       by this program was not closed properly. To fix, you'll have to end
#       your ssh session and sign back in or restart the program and use 
#       the spacebar to quit the program correctly. 

import os, sys
import create
import time
import curses

# Change the roomba port to whatever is on your
# machine. On a Mac it's something like this.
# On Linux it's usually tty.USB0 and on Win
# its to serial port.
ROOMBA_PORT = "/dev/ttyUSB0"

robot = create.Create(ROOMBA_PORT, BAUD_RATE=115200)
robot.toSafeMode()

FWD_CMPS = 20 # forward speed in cm per second
ROT_CMPS = 60 # rotation speed in cm per second
TURN_DELAY = 6.55 / 6 # in seconds 90 degree turns dependent on ROT_CMPS == 60
FWD_DELAY = 34 / FWD_CMPS # roomba's diameter is 34 cm and adjusting based on FWD_CMPS

def move_roomba(mult, robot_dir, robot_rot):
     robot.go(FWD_CMPS * robot_dir * mult, ROT_CMPS * robot_rot * mult)
     if robot_dir == 0:
        time.sleep(TURN_DELAY)
     else: 
         time.sleep(FWD_DELAY)
     robot.go(0,0)

def main():
        screen = curses.initscr()
        curses.cbreak()
        screen.keypad(True)

	robot.resetPose()
        robot_dir = 0
        robot_rot = 0
        mult = 1.0

	while True:
            mult = 1.0
            input = screen.getch()
            robot_dir = 0
            robot_rot = 0
            if input == ord(' '):
	            break
	    elif input == ord('w'):
		robot_dir = 1
	    elif input == ord('s'):
		robot_dir = -1
	    elif input == ord('a'):
		robot_rot = 1
                mult = 1.5
	    elif input == ord('d'):
		robot_rot = -1
                mult = 1.5
            elif input == ord('z'):
                robot_rot = 1
                mult = 1.2
            elif input == ord('c'):
                robot_rot = -1
                mult = 1.2
            elif input == ord('q'):
                robot_rot = 1
                mult = 0.4
            elif input == ord('e'):
                robot_rot = -1
                mult = 0.4

            move_roomba(mult, robot_dir, robot_rot)
            #screen.addch('y')

if __name__ == '__main__': 
    try:    
        main()
    except Exception as err:
	print (err)
    
    robot.go(0,0)
    robot.close()
    curses.nocbreak()
    curses.echo()
    curses.endwin()
