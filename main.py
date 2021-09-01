from MangaeGroup import ManageGroup
from Info import Info
import logging
import threading
import time
import os
import sys

def ShowThreadFunc(info):
    while(True):
        infoState=info.CollectInfo()
        if infoState==True:
            os.system('cls' if os.name == 'nt' else 'clear')
            info.ShowInfo()
        time.sleep(1)


logging.basicConfig(level=logging.WARN)
argv= sys.argv
group= ManageGroup(argv[1])
info= Info(group.GetCodes())
x= threading.Thread(target=ShowThreadFunc,args=(info,))
x.start()



