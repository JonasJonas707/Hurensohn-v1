import ssl, os, requests, time
from threading import active_count, Thread
from pystyle import Colorate, Colors, Write
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
from Data.UserAgent import UserAgent
from Data.Lists import DeviceTypes, Platforms, Channel, ApiDomain

Debug = Write.Input("Shares oder Likes [S/L] ? > ", Colors.red_to_blue, interval=0.0001)
        if Debug.lower().startswith("S"):
            run(ShareBot.py) 
        else:
            DebugMode = False
