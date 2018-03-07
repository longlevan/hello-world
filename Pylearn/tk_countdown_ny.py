"""
countdown to the deadline using Tkinter 
use update() after sleep()
"""
try:
    # python 2
    import Tkinter as tk
except ImportError as identifier:
    # python 3
    import tkinter as tk
import time

class countdownclock():
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    
    def Update(self,**kwargs):
        self.__dict__.update(kwargs)
    
    def countDown(self):
        """start coundown 10 seconds before """
        lbl.config(bg = 'yellow')
        for k in range(10,-1,-1):
            lbl["text"]=k
            time.sleep(1)
            root.update() # tk needs this after sleep
        lbl.config(bg='red')
        lbl["text"]="Happy new year!"
