'''
Created on Oct 6, 2019

@author: romina
'''

import numpy as np


class Point():
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property
    def xy(self):
        return (self._x, self._y)

class PolarPoint():
    def __init__(self, rho=0, phi=0):
        """
        Parametros
        ---------
        rho: distancia al centro
        phi: angulo respecto al centro (deg)
        """
        self._phi = phi
        self._rho = rho

    @property
    def phi(self):
        return self._phi

    @phi.setter
    def phi(self, phi):
        self._phi = phi

    @property
    def rho(self):
        return self._rho

    @rho.setter
    def rho(self, rho):
        self._rho = rho
        
    def cart(self):
        return self.pol2cart(self)

    @staticmethod
    def cart2pol(point):
        rho = np.sqrt(point.x**2 + point.y**2)
        phi = np.arctan2(point.x, point.y)
        return PolarPoint(rho, np.rad2deg(phi))

    @staticmethod
    def pol2cart(polar):
        x = polar.rho * np.cos(np.deg2rad(polar.phi))
        y = polar.rho * np.sin(np.deg2rad(polar.phi))
        return Point(x, y)
