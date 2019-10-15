'''
Created on Oct 6, 2019

@author: romina
'''

import numpy as np

class Triangulo():
    def __init__(self, vert1, vert2, vert3):
        """
        Triangulo de vertices dados

        Parametros
        ----------
        vert1: (Point), vert2: (Point), vert3: (Point) 
        """
        self._v1 = vert1
        self._v2 = vert2
        self._v3 = vert3
    
    def orientacion(self):
        """
        Devuelve la orientacion del triangulo
        """
        return (self._v1.x - self._v3.x) * (self._v2.y - self._v3.y) - (self._v1.y - self._v3.y) * (self._v2.x - self._v3.x)

    def perimetro(self):
        """
        Devuelve el perimetro del triangulo
        """
        a = np.array(self._v1.xy)
        b = np.array(self._v2.xy)
        c = np.array(self._v3.xy)
        ab = b - a
        bc = c - b
        ca = a - c
        return np.sqrt(ab[0]**2 + ab[1]**2) + np.sqrt(bc[0]**2 + bc[1]**2) + np.sqrt(ca[0]**2 + ca[1]**2)


    def angulos(self):
        """
        Devuelve los angulos internos
        """
        a = np.array(self._v1.xy)
        b = np.array(self._v2.xy)
        c = np.array(self._v3.xy)
        ab = b - a
        bc = c - b
        ca = a - c
        la = np.sqrt(np.math.pow(ab[0], 2) + np.math.pow(ab[1], 2))
        lb = np.sqrt(np.math.pow(bc[0], 2) + np.math.pow(bc[1], 2))
        lc = np.sqrt(np.math.pow(ca[0], 2) + np.math.pow(ca[1], 2))
        alfa = np.math.acos((np.math.pow(lb, 2) + np.math.pow(lc, 2) - np.math.pow(la, 2)) / (2*lb*lc))
        beta = np.math.acos((np.math.pow(la, 2) + np.math.pow(lc, 2) - np.math.pow(lb, 2)) / (2*la*lc))
        gamma = np.pi - alfa - beta
        
        return (alfa, beta, gamma)

    def area(self):
        """
        Devuelve el area del triangulo
        """
        return abs((self._v1.x - self._v3.x) * (self._v2.y - self._v1.y) - (self._v1.x - self._v2.x) * (self._v3.y - self._v1.y)) * 0.5

    def p_dentro(self, pos4):
        """
        Verifica que un punto este dentro del triangulo
        comparando la orientacion del triangulo con
        la orientacion de los triangulos formados por reemplazar
        un vertice con la posicion pos4

        Parametros
        ----------
        pos4: punto a validar (Point)
        """
        orientacion = self.orientacion()
        orientacion1 = Triangulo(self._v1, self._v2, pos4).orientacion()
        orientacion2 = Triangulo(self._v2, self._v3, pos4).orientacion()
        orientacion3 = Triangulo(self._v3, self._v1, pos4).orientacion()
        if orientacion >= 0 and orientacion1 >= 0 and orientacion2 >= 0 and orientacion3 >= 0:
            return True
        if orientacion <= 0 and orientacion1 <= 0 and orientacion2 <= 0 and orientacion3 <= 0:
            return True
        return False
