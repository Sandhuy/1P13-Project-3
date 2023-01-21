import time
import random
import sys
sys.path.append('../')

from Common_Libraries.p3b_lib import *

import os
from Common_Libraries.repeating_timer_lib import repeating_timer

def update_sim():
    try:
        my_table.ping()
    except Exception as error_update_sim:
        print (error_update_sim)

### Constants
speed = 0.2 #Qbot's speed

### Initialize the QuanserSim Environment
my_table = servo_table()
arm = qarm()
arm.home()
bot = qbot(speed)

##---------------------------------------------------------------------------------------
## STUDENT CODE BEGINS
##---------------------------------------------------------------------------------------
#We define a function for dispensing Container. We defined the material, mass and ContainerID
# by inputing the computer value
# After defining them we have another function for dispensing the container. We return the mass and ID
# because these are the constriants

def dispense_container(): 
    material, mass, ID_Bin = my_table.conatiner_properties(int(input("Container ID: ")))
    my_table.dispense_container()
    return mass, ID_Bin

def load_containers():
    
    


##---------------------------------------------------------------------------------------
## STUDENT CODE ENDS
##---------------------------------------------------------------------------------------
update_thread = repeating_timer(2,update_sim)
