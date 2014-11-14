'''
Created on Oct 3, 2014

@author: mike
'''
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Line
from math import cos, sin, pi
from kivy.clock import Clock
from functools import partial


# Use RelativeLayout so this can be wired into another app
class CountDownTimer(RelativeLayout):
      
    def __init__self(self, **kwargs):
        self.face = Face()
        self.hand = TimerHand()
       
    def get_seconds(self):
        num_str = self.seconds_input.text
        return num_str
   
    def start_hand(self):
        self.hand.draw_hand(0)
        et = int(self.get_seconds())
        # divisor to create more or fewer drawing cncrements 1 = 1 secone/ 60 = 1/60 second
        speed_dial = 60.0
        # try to get smaller increments of hand drawing    
        angle_increment = et * speed_dial 
        i = 1
        while i < (angle_increment+1):
            angle = (360.0/angle_increment) * i
            interval = i/speed_dial
            Clock.schedule_once(partial(self.hand.draw_hand, angle), interval)
            i += 1
              
class Face(Widget):
    pass


class TimerHand(Widget):
        
    def draw_hand(self, angle, *args):
        self.canvas.clear()
        with self.canvas:
            Color(.7, .93, .05)
            Line(points = [self.center_x, self.center_y, (self.center_x + 0.6*self.r*sin(pi/180*angle)), 
                   self.center_y + 0.6*self.r*cos(pi/180*angle)], width = 4, cap = "round")
            # print str(angle) + 'in draw_hand'


class SimpleTimerApp(App):
    def build(self):
        return CountDownTimer()


if __name__ == '__main__':
    SimpleTimerApp().run()
