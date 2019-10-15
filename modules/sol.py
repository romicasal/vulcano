'''
Created on Oct 6, 2019

@author: romina
'''

from cuerpo_celeste import CuerpoCeleste

class Sol(CuerpoCeleste):
    def __init__(self):
        super(Sol, self).__init__("Sol", 0, 0)
