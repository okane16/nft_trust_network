import numpy as np
import frame


class window:

    def __init__ (self):
        self.frames = {}
        self.m = 0
        self.e = 0

    def addToWindow(date, score):
        ## if tweet is from a new day not in our window, create a new frame for this day
        if (date not in frames):
            frames[date] = frame()
        
        ## add tweet sentiment score to frame
        frames[date].add_measure(score)
    
    def calculate_m():
        numerator_sum = 0
        denominator_sum = 0
        
        for date, frame in frames.items():
            (m_i, c_i) = frame.get_measures()
            numerator_sum += (m_i * c_i)
            denominator_sum += c_i
       
       return (numerator_sum / denominator_sum)

