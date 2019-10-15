'''
Created on Oct 6, 2019

@author: romina
'''

from utiles.point import PolarPoint
from utiles.figura import Triangulo

class CuerpoCeleste():
    """
    Abstraccion de cualquier cuerpo del sistema solar

    Parametros
    ----------
    nombre : nombre del CuerpoCeleste
    angulo : angulo inicial respecto al centro (deg)
    distancia : distancia al centro del sistema solar
    """
    ORBITA = 360
    MIN_PHI = -1 * ORBITA
    MAX_PHI = ORBITA

    def __init__(self, nombre, angulo, distancia):
        if not self.MIN_PHI <= angulo <= self.MAX_PHI:
            raise ValueError("El angulo debe estar entre %s y %s." \
                             % (self.MIN_PHI, self.MAX_PHI))
        self._nombre = nombre
        self._pos = PolarPoint(abs(distancia), angulo)

    @property
    def nombre(self):
        return self._nombre

    @property
    def pos(self):
        return self._pos

    @staticmethod
    def alineados(c1, c2, c3):
        """
        Verifica que tres CuerpoCelestes esten alineados
        Devuelve True si el area del triangulo formada por los tres puntos es cero
        """
        # para que funcione como casi_alineados usar EPSILON = 30000
        EPSILON = 0.0001 
        return Triangulo(
            PolarPoint.pol2cart(c1.pos),
            PolarPoint.pol2cart(c2.pos),
            PolarPoint.pol2cart(c3.pos)).area() <= EPSILON

    @staticmethod
    def casi_alineados(c1, c2, c3):
        """
        Verifica que tres CuerpoCelestes esten casi alineados
        Devuelve True si al menos uno de sus angulos internos es < MAX_ANG
        """
        MAX_ANG = 0.03
        alfa, beta, gamma = Triangulo(
            PolarPoint.pol2cart(c1.pos),
            PolarPoint.pol2cart(c2.pos),
            PolarPoint.pol2cart(c3.pos)).angulos()
        return abs(alfa) < MAX_ANG or abs(beta) < MAX_ANG or abs(gamma) < MAX_ANG

    @staticmethod
    def encierran(c1, c2, c3, c4):
        """
        Verifica que tres cuerpos celestes (c1...c3) encierren a otro (c4)
        """
        return Triangulo(
            PolarPoint.pol2cart(c1.pos),
            PolarPoint.pol2cart(c2.pos),
            PolarPoint.pol2cart(c3.pos)).p_dentro(PolarPoint.pol2cart(c4.pos))

    @staticmethod
    def sumar_distancias(c1, c2, c3):
        """
        Devuelve la distancia total para recorrer todos los CuerpoCelestes
        (es decir el perimetro total del triangulo que forman)
        """
        return Triangulo(PolarPoint.pol2cart(c1.pos),
                         PolarPoint.pol2cart(c2.pos),
                         PolarPoint.pol2cart(c3.pos)).perimetro()

    def __dict__(self):
        return dict(nombre=self._nombre,
                    phi=self._pos.phi,
                    rho=self._pos.rho)
