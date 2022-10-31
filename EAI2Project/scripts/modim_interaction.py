import importlib
import os
import sys
import time
import subprocess
import argparse
from PIL import Image, ImageDraw, ImageFont
try:
    sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
    print "Please set MODIM_HOME environment variable to MODIM folder."
    sys.exit(1)

import ws_client
from ws_client import *

class TabletInteraction():
    
    def __init__(self,do_):
        mws = ModimWSClient()
        mws.setDemoPathAuto(__file__)
        if(do_=="i1"):
            mws.run_interaction(self.i1)
        else: mws.run_interaction(self.i2)
    
    def i1(self):
        im.init()
        
        a = im.ask('indications', timeout = -1)
        if(a!="timeout"):
            im.display.loadUrl('grid.html')
            a = im.ask(a,timeout=-1)
            print(os.getcwd())
            with open("/home/robot/playground/html/sample/utils/obs.out","w") as f:
                f.write(a)
                f.close()
            
    
    def i2(self):
        im.init()
        a = im.ask('game',timeout= -1)
        if(a!="timeout"):
            im.display.loadUrl('game.html')
            im.ask('quit',timeout=-1)
            
    def i3(self):
        im.display.loadUrl('showpath.html')
        im.ask('quit',timeout=-1)
class Reset:

    def __init__(self):
        mws = ModimWSClient()
        mws.setDemoPathAuto(__file__)
        mws.run_interaction(self.i1)

    def i1(self):
        im.init()