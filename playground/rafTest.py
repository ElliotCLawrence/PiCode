
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
TURN_DELAY = 6.55 / 6 # in seconds 90 degree turns dependent on ROT_CMPS == 60
FWD_DELAY = 34 / FWD_CMPS # roomba's diameter is 34 cm and adjusting based on FWD_CMPS

def move_roomba(mult, robot_dir, robot_rot):
     robot.go(FWD_CMPS * robot_dir * mult, ROT_CMPS * robot_rot * mult)
     if robot_dir == 0:
        time.sleep(TURN_DELAY)
     else: 
         time.sleep(FWD_DELAY);
     robot.go(0,0)

def main():
        screen = curses.initscr()
        # curses.noecho()
        curses.cbreak()
        screen.keypad(True)

	robot.resetPose()
        robot_dir = 0;
        robot_rot = 0;
        mult = 1.0;
	# px, py, th = robot.getPose()

	while True:
            mult = 1.0;
            input = screen.getch()
            robot_dir = 0;
            robot_rot = 0;
            if input == ord(' '):
	        break;
	    elif input == ord('w'):
		robot_dir = 1;
	    elif input == ord('s'):
		robot_dir = -1;
	    elif input == ord('a'):
		robot_rot = 1;
                mult = 1.5;
	    elif input == ord('d'):
		robot_rot = -1;
                mult = 1.5;
            elif input == ord('z'):
                robot_rot = 1;
                mult = 1.2;
            elif input == ord('c'):
                robot_rot = -1;
                mult = 1.2;
            elif input == ord('q'):
                robot_rot = 1;
                mult = 0.4;
            elif input == ord('e'):
                robot_rot = -1;
                mult = 0.4;

            move_roomba(mult, robot_dir, robot_rot);
            #screen.addch('y')

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
