from plyer import battery
import time
from sender import Sender
import location
def main():
    now = time.time()#seting the start of usin0
    while True:
        if battery.status['percentage'] <= 1:#checking the battery's level 
            Sender(open('data.txt', 'r').read(), location.loc())#sending location to recipient
            break
        else:
            time.sleep(60)#waiting 60 seconds to the next check    
