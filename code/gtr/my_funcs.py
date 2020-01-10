# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 08:08:55 2020

@author: eng_g
"""
import numpy as np

def curve_params(curve_type):
    """Returns the tripping curve parameters according to its type"""
    if curve_type == 'B':
        par_A = 1.4636
        par_B = 0
        par_C = 1
        par_K = 0.028
        par_N = 1.0469
    elif curve_type == 'A':
        par_A = 0.01414
        par_B = 0
        par_C = 1
        par_K = 0.028
        par_N = 0.02
        
    return par_A, par_B, par_C, par_K, par_N

class bassler_be1_851():
    
    def __init__(self, PU, DT, curve_type, DI=1000000):
        """Initialization of overcurrent relay
        Inputs:
            PU: pick-up current (A)
            DI: instantaneous trip current (A)
            DT: time dial
            curve_type: A or B
            """
        self.PU = PU
        self.DI = DI
        self.DT = DT
        self.A, self.B, self.C, self.K, self.N = curve_params(curve_type)
        self.curve_type = curve_type

    def time_current_curve(self):
        """ Relay inverse time characteristic curve """
        
        current = self.PU*np.logspace(0.0001, 3, num=200)
        
        time = ((self.A*self.DT) / (current**self.N - self.C)) + self.B*self.DT \
                                                                + self.K    
 
        current[current > self.DI] = self.DI
        
        return current, time
    
class iec_relay():
    
    def __init__(self, PU, DT, curve_type, DI=1000000):
        """Initialization of overcurrent relay
        Relays:
            BBC IC 91
            INEPAR IN
        
        Inputs:
            PU: pick-up current (A)
            DI: instantaneous trip current (A)
            DT: time dial
            curve_type: normal/standard inverse 'NI', very inverse 'VI',
                        extrmely inverse 'EI' or long time earth fault 'LTEF'
            """
        self.PU = PU
        self.DI = DI
        self.DT = DT
        self.curve_type = curve_type

    def time_current_curve(self):
        """ Relay inverse time characteristic curve """
        
        current = np.logspace(0.0001, 3, num=200)
        
        if self.curve_type == 'EI':
            time = self.DT * 80 / ((current ** 2) - 1)
        elif self.curve_type == 'NI':
            time = self.DT * 0.14 / ((current ** 0.02) - 1)
        elif self.curve_type == 'VI':
            time = self.DT * 13.5 / (current - 1)
        else:
            time = self.DT * 120 / (current - 1)
                
        current = self.PU*current
        current[current > self.DI] = self.DI
        
        return current, time

class definite_time_relay():
    
    def __init__(self, PU, DT):
        """Initialization of overcurrent relay
        Relays:
            INEPAR ID
        
        Inputs:
            DT: time dial
        """
        
        self.PU = PU
        self.DT = DT

    def time_current_curve(self):
        """ Relay definite time characteristic curve """
        
        current = np.logspace(0.0001, 3, num=200)
        
        time = self.DT*np.ones(len(current))
                
        current = self.PU*current
        
        return current, time

