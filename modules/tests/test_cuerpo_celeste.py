'''
Created on Oct 7, 2019

@author: romina
'''

import unittest
import math
from cuerpo_celeste import CuerpoCeleste

class TestCuerpoCeleste(unittest.TestCase):


    def test_alineados_true(self):
        c1 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=500)
        c2 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=1000)
        c3 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=2000)

        self.assertTrue(CuerpoCeleste.alineados(c1, c2, c3))

        c1 = CuerpoCeleste(nombre="Tierra", angulo=45, distancia=500)
        c2 = CuerpoCeleste(nombre="Tierra", angulo=45, distancia=1000)
        c3 = CuerpoCeleste(nombre="Tierra", angulo=45, distancia=2000)

        self.assertTrue(CuerpoCeleste.alineados(c1, c2, c3))
        
    def test_alineados_false(self):
        c1 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=500)
        c2 = CuerpoCeleste(nombre="Tierra", angulo=1, distancia=1000)
        c3 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=2000)

        self.assertFalse(CuerpoCeleste.alineados(c1, c2, c3))

        c1 = CuerpoCeleste(nombre="Tierra", angulo=30, distancia=500)
        c2 = CuerpoCeleste(nombre="Tierra", angulo=35, distancia=1000)
        c3 = CuerpoCeleste(nombre="Tierra", angulo=30, distancia=2000)

        self.assertFalse(CuerpoCeleste.alineados(c1, c2, c3))


    def test_casi_alineados_true(self):
        c1 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=500)
        c2 = CuerpoCeleste(nombre="Tierra", angulo=1, distancia=1000)
        c3 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=2000)

        self.assertTrue(CuerpoCeleste.casi_alineados(c1, c2, c3))

        c1 = CuerpoCeleste(nombre="Tierra", angulo=1, distancia=500)
        c2 = CuerpoCeleste(nombre="Tierra", angulo=2, distancia=1000)
        c3 = CuerpoCeleste(nombre="Tierra", angulo=1, distancia=2000)

        self.assertTrue(CuerpoCeleste.casi_alineados(c1, c2, c3))

        c1 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=500)
        c2 = CuerpoCeleste(nombre="Tierra", angulo=2, distancia=1000)
        c3 = CuerpoCeleste(nombre="Tierra", angulo=4, distancia=2000)

        self.assertTrue(CuerpoCeleste.casi_alineados(c1, c2, c3))


    def test_casi_alineados_false(self):
        c1 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=150)
        c2 = CuerpoCeleste(nombre="Marte", angulo=2, distancia=230)
        c3 = CuerpoCeleste(nombre="Venus", angulo=0, distancia=108)

        self.assertFalse(CuerpoCeleste.casi_alineados(c1, c2, c3))

        c1 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=150)
        c2 = CuerpoCeleste(nombre="Marte", angulo=2, distancia=230)
        c3 = CuerpoCeleste(nombre="Venus", angulo=5, distancia=108)

        self.assertFalse(CuerpoCeleste.casi_alineados(c1, c2, c3))

        c1 = CuerpoCeleste(nombre="Tierra", angulo=1, distancia=150)
        c2 = CuerpoCeleste(nombre="Marte", angulo=2, distancia=230)
        c3 = CuerpoCeleste(nombre="Venus", angulo=5, distancia=108)
        
        self.assertFalse(CuerpoCeleste.casi_alineados(c1, c2, c3))

    def test_encierran_true(self):
        c1 = CuerpoCeleste(nombre="Tierra", angulo=160, distancia=150)
        c2 = CuerpoCeleste(nombre="Marte", angulo=30, distancia=230)
        c3 = CuerpoCeleste(nombre="Venus", angulo=270, distancia=108)
        c4 = CuerpoCeleste(nombre="Sol", angulo=0, distancia=0)

        self.assertTrue(CuerpoCeleste.encierran(c1, c2, c3, c4))

    def test_encierran_false(self):
        c1 = CuerpoCeleste(nombre="Tierra", angulo=160, distancia=150)
        c2 = CuerpoCeleste(nombre="Marte", angulo=290, distancia=230)
        c3 = CuerpoCeleste(nombre="Venus", angulo=270, distancia=108)
        c4 = CuerpoCeleste(nombre="Sol", angulo=0, distancia=0)

        self.assertFalse(CuerpoCeleste.encierran(c1, c2, c3, c4))

    def test_sumar_distancias(self):
        c1 = CuerpoCeleste(nombre="Tierra", angulo=0, distancia=100)
        c2 = CuerpoCeleste(nombre="Marte", angulo=90, distancia=200)
        c3 = CuerpoCeleste(nombre="Venus", angulo=180, distancia=300)
    
        self.assertTrue(math.isclose(
            CuerpoCeleste.sumar_distancias(c1, c2, c3),
            984.161925296))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()