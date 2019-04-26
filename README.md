# Piloting a Roomba via SSH

Included within this repo, there is a `create.py` file which was provided by the following repository: https://github.com/martinschaef/roomba. This file was necessary in interfacing with Roomba. With this, you can run the `runRoomba.py` to pilot the roomba. 

# Instructions to pilot the roomba: 
* Connect the raspberry pi to the roomba
* ssh into the raspberry pi
* Run `python roomba runRoomba.py`
* Pilot Roomba:
    * Use `a` and `s` to make ~90 degree rotations
    * Use `q` and `e` to make ~45 degree rotations
    * Use `w` and `s` to make move roomba fowards or backwards
    * Use `(spacebar)` to quit application

# Notes:
* Refrain from holding down buttons as each button logged 
      will result in the corresponding action (unable to be stopped)
* If spacebar is not hit to quit, the terminal is still functional
      but may have formatting issues because the console screen initialized
      by this program was not closed properly. To fix, you'll have to end
      your ssh session and sign back in or restart the program and use 
      the spacebar to quit the program correctly. 