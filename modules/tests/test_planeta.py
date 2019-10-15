'''
Created on Oct 7, 2019

@author: romina
'''

import unittest
from planeta import Planeta

class TestPlaneta(unittest.TestCase):


    def test_crear_planeta_ok(self):
        Planeta(nombre="Tierra", angulo=0, distancia=100,
                velocidad=1, sentido=1)

    def test_crear_planeta_distancia_negativa_ok(self):
        Planeta(nombre="Tierra", angulo=0, distancia=-100,
        velocidad=1, sentido=1)

    def test_crear_planeta_angulo_limite_ok(self):
        Planeta(nombre="Tierra", angulo=-360, distancia=100,
                velocidad=1, sentido=1)
        Planeta(nombre="Tierra", angulo=0, distancia=100,
                velocidad=1, sentido=1)
        Planeta(nombre="Tierra", angulo=360, distancia=100,
                velocidad=1, sentido=1)

    def test_crear_planeta_fuera_angulo_raises_valueerror(self):
        self.assertRaises(
            ValueError,
            Planeta, nombre="Tierra", angulo=-361, distancia=100,
            velocidad=1, sentido=1)
        self.assertRaises(
            ValueError,
            Planeta, nombre="Tierra", angulo=361, distancia=100,
            velocidad=1, sentido=1)

    def test_crear_planeta_fuera_distancia_cero_raises_valueerror(self):
        self.assertRaises(
            ValueError,
            Planeta, nombre="Tierra", angulo=0, distancia=0,
            velocidad=1, sentido=1)

    def test_crear_planeta_sentido_raises_valueerror(self):
        self.assertRaises(
            ValueError,
            Planeta, nombre="Tierra", angulo=0, distancia=100,
            velocidad=1, sentido=2)
        self.assertRaises(
            ValueError,
            Planeta, nombre="Tierra", angulo=0, distancia=100,
            velocidad=1, sentido=-2)

    def test_mover_planeta_sentido_horario_angulo_ok(self):
        planeta1 = Planeta(nombre="Tierra", angulo=0, distancia=100,
                velocidad=1, sentido=-1)
        planeta1.step()
        self.assertEqual(planeta1.pos.phi, 360-1)
        planeta1.step()
        self.assertEqual(planeta1.pos.phi, 360-2)
        
        planeta2 = Planeta(nombre="Tierra", angulo=0, distancia=100,
                velocidad=3, sentido=-1)
        planeta2.step()
        self.assertEqual(planeta2.pos.phi, 360-3)
        planeta2.step()
        self.assertEqual(planeta2.pos.phi, 360-6)

        planeta3 = Planeta(nombre="Tierra", angulo=360, distancia=100,
                velocidad=5, sentido=-1)
        planeta3.step()
        self.assertEqual(planeta3.pos.phi, 360-5)
        planeta3.step()
        self.assertEqual(planeta3.pos.phi, 360-10)

        planeta4 = Planeta(nombre="Tierra", angulo=90, distancia=100,
                velocidad=5, sentido=-1)
        planeta4.step()
        self.assertEqual(planeta4.pos.phi, 90-5)
        planeta4.step()
        self.assertEqual(planeta4.pos.phi, 90-10)

    def test_mover_planeta_sentido_antihorario_angulo_ok(self):
        planeta1 = Planeta(nombre="Tierra", angulo=0, distancia=100,
                velocidad=1, sentido=1)
        planeta1.step()
        self.assertEqual(planeta1.pos.phi, 1)
        planeta1.step()
        self.assertEqual(planeta1.pos.phi, 2)
        
        planeta2 = Planeta(nombre="Tierra", angulo=0, distancia=100,
                velocidad=3, sentido=1)
        planeta2.step()
        self.assertEqual(planeta2.pos.phi, 3)
        planeta2.step()
        self.assertEqual(planeta2.pos.phi, 6)

        planeta3 = Planeta(nombre="Tierra", angulo=360, distancia=100,
                velocidad=5, sentido=1)
        planeta3.step()
        self.assertEqual(planeta3.pos.phi, 5)
        planeta3.step()
        self.assertEqual(planeta3.pos.phi, 10)

        planeta4 = Planeta(nombre="Tierra", angulo=90, distancia=100,
                velocidad=5, sentido=1)
        planeta4.step()
        self.assertEqual(planeta4.pos.phi, 95)
        planeta4.step()
        self.assertEqual(planeta4.pos.phi, 100)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()