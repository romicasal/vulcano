'''
Created on Oct 6, 2019

@author: romina
'''

from cuerpo_celeste import CuerpoCeleste

class Planeta(CuerpoCeleste):
    """
    Un planeta es un cuerpo celeste que orbita alrededor del sol

    Parametros
    ----------
    nombre : nombre del Planeta
    distancia : distancia al centro del sistema solar
    angulo : angulo inicial respecto al centro (deg)
    velocidad : velocidad angular (>0) medida como grados(deg) / dia
    sentido : sentido -1 horario 1 antihorario
    """

    def __init__(self, nombre, angulo, distancia, velocidad, sentido):
        if velocidad <= 0:
            raise ValueError("La velocidad debe ser mayor a cero.")
        if abs(sentido) != 1:
            raise ValueError("El sentido debe ser -1 (horario) 1 (antihorario).")
        if distancia == 0:
            raise ValueError("La distancia al centro no puede ser nula.")
        
        super(Planeta, self).__init__(nombre, angulo, distancia)
        self._w = velocidad
        self._s = sentido

    def step(self):
        """
        Avanza segun la velocidad y el sentido definido
        """
        new_phi = self._pos.phi + self._w * self._s
        if 0.0 < new_phi < self.ORBITA:
            self._pos.phi = new_phi
        elif new_phi > 0.0:
            self._pos.phi = new_phi - self.ORBITA
        else:
            self._pos.phi = new_phi + self.ORBITA


    def __dict__(self):
        basedict = super(Planeta, self).__dict__()
        basedict.update(dict(
            velocidad=self._w,
            sentido=self._s))
        return basedict
