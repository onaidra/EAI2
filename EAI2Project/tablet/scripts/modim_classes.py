import sys
import os
import time

try:
    sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
    print "Please set MODIM_HOME environment variable to MODIM folder."
    sys.exit(1)

import ws_client
from ws_client import *

class Lessons:

    def __init__(self, mode='BEGINNER', allow_choice=False):
        mws = ModimWSClient()
        mws.setDemoPathAuto(__file__)
        if mode == 'BEGINNER':
            if allow_choice:
                mws.run_interaction(self.i0)
            else:
                mws.run_interaction(self.i1)
        elif mode == 'INTERMEDIATE':
            if allow_choice:
                mws.run_interaction(self.i2)
            else:
                mws.run_interaction(self.i3)
        else:
            if allow_choice:
                mws.run_interaction(self.i4)
            else:
                mws.run_interaction(self.i5)

    def i0(self):
        im.display.loadUrl('beginner_choice.html')

    def i1(self):
        a = im.ask('start_lessons', timeout=-1)
        if (a != 'timeout'):
            im.display.loadUrl('beginner_lesson1.html')

    def i2(self):
        im.display.loadUrl('intermediate_choice.html')

    def i3(self):
        a = im.ask('start_lessons', timeout=-1)
        if (a != 'timeout'):
            im.display.loadUrl('intermediate_lesson1.html')

    def i4(self):
        im.display.loadUrl('expert_choice.html')

    def i5(self):
        a = im.ask('start_lessons', timeout=-1)
        if (a != 'timeout'):
            im.display.loadUrl('expert_lesson1.html')


class CleanScreen:

    def __init__(self):
        mws = ModimWSClient()
        mws.setDemoPathAuto(__file__)
        mws.run_interaction(self.i1)

    def i1(self):
        im.init()
