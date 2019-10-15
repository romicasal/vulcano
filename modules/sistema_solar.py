'''
Created on Oct 6, 2019

@author: romina
'''

from clima import Clima
from cuerpo_celeste import CuerpoCeleste
from sol import Sol

class SistemaSolar():

    CANT_PLANETAS = 3

    def __init__(self, planetas, dia=0):
        """
        Parametros
        ----------
        planetas: arreglo de 3 planetas (planeta1, planeta2, planeta3)
        dia: dia actual
        """
        self._clima = Clima()
        self._sol = Sol()
        self._dia = dia
        if len(planetas) != SistemaSolar.CANT_PLANETAS:
            raise ValueError("El sistema debe tener %s planetas")
        self._planetas = planetas

    @property
    def dia(self):
        return self._dia

    @property
    def planetas(self):
        return self._planetas
    
    def do_step(self):
        """
        Incrementa la cantidad de dias
        Devuelve el clima del dia actual
        """
        self._dia += 1
        for planeta in self._planetas:
            planeta.step()
        return self._clima.registrar_clima(self)

    def pronostico_clima(self):
        """
        Devuelve el pronostico del clima para los dias registrados
        """
        return self._clima.pronostico()
    
    def planetas_alineados(self):
        """
        Verifica si los planetas estan alineados
        """
        return CuerpoCeleste.casi_alineados(*self._planetas)

    def sistema_alineado(self):
        """
        Verifica si dos planetas estan alineados con el sol
        """
        c1, c2, _ = self._planetas
        return CuerpoCeleste.alineados(c1, c2, self._sol) and \
            self.planetas_alineados()
    
    def sol_encerrado(self):
        """
        Verifica si el sol queda encerrado entre los planetas
        """
        c1, c2, c3 = self._planetas
        return CuerpoCeleste.encierran(c1, c2, c3, self._sol)
    
    def distancia_entre_planetas(self):
        """
        Devuelve la distancia entre los planetas cuando forman un triangulo
        Suponiendo A,B,C planetas: dist(BA) + dist(CB) + dist(AC)
        """
        return CuerpoCeleste.sumar_distancias(*self._planetas)
