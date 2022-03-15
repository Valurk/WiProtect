import pyshark
import os
import sys

from termcolor import colored


if not os.geteuid()==0:
    sys.exit('This script must be run as root!')


os.system('sudo airmon-ng check kill') # kill any processes that might interfere with this script
os.system('clear')

os.system('sudo airmon-ng start wlan0') # putting the interface in the monitor mode for capture the packets
os.system('clear')

class style():
    
    RED = '\033[31m'
    GREEN = '\033[32m'
    

print(style.GREEN + '''
 __          ___ _____           _            _   
 \ \        / (_)  __ \         | |          | |  
  \ \  /\  / / _| |__) | __ ___ | |_ ___  ___| |_ 
   \ \/  \/ / | |  ___/ '__/ _ \| __/ _ \/ __| __|
    \  /\  /  | | |   | | | (_) | ||  __/ (__| |_ 
     \/  \/   |_|_|   |_|  \___/ \__\___|\___|\__|
                                                                                                          
''')
#effetct blink on text
import time
for _ in range(5):
    for x in range (4): # three dots
        string = "Waiting for packets" + "." * x + "   "
        print (style.GREEN +string, end="\r")
        


captureAndFilter = pyshark.LiveCapture(interface='wlan0mon',display_filter = 'wlan.fixed.reason_code != 0x0003') #reason code correctly is 0x0003
#for packet in capture.sniff_continuously():

for packet in captureAndFilter:
    print(captureAndFilter, end='\r') #reformatting the original output is: <LiveCapture (0 packets)>
    print(style().RED + "DEAUTH ATTACK DETECTED!  ") 
