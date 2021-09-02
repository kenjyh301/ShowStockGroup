from ManageGroup import ManageGroup
from Info import Info
import logging
import threading
import time
import os

# import sys



def ShowThreadFunc(info):
    while(True):
        infoState=info.CollectInfo()
        if infoState==True:
            os.system('cls' if os.name == 'nt' else 'clear')
            info.ShowInfo()
        time.sleep(1)

if __name__=="__main__":
    logging.basicConfig(level=logging.WARN)
    # argv= sys.argv
    # group= ManageGroup('CurrentHold.csv')
    groupName= input("Please enter group: ")
    group= ManageGroup(groupName)
    info= Info(group.GetCodes())
    x= threading.Thread(target=ShowThreadFunc,args=(info,))
    x.start()
    





