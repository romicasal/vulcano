'''
Created on Oct 6, 2019

@author: romina
'''


import itertools
from _operator import itemgetter

class Clima():
    
    CLIMAS = {'NORMAL': 'Normal', 'LLUVIA': 'Lluvia', 'SEQUIA': 'Sequia', 'OPTIMO': 'Optimo'}
    
    def __init__(self):
        self._registro = []
        self._pico_lluvia = None
    
    def _agregar_dia(self, dia, estado, distancias=0):
        self._registro.append(dict(dia=dia, estado=estado, distancias=distancias))
        if estado == Clima.CLIMAS['LLUVIA'] and \
            (not self._pico_lluvia or self._pico_lluvia['distancias'] < distancias):
            self._pico_lluvia = dict(dia=dia, estado=estado, distancias=distancias)
    
    def _agregar_dia_normal(self, dia):
        self._agregar_dia(dia, Clima.CLIMAS['NORMAL'])

    def _agregar_dia_lluvia(self, dia, distancias):
        self._agregar_dia(dia, Clima.CLIMAS['LLUVIA'], distancias)

    def _agregar_dia_sequia(self, dia):
        self._agregar_dia(dia, Clima.CLIMAS['SEQUIA'])

    def _agregar_dia_optimo(self, dia):
        self._agregar_dia(dia, Clima.CLIMAS['OPTIMO'])

    
    def registrar_clima(self, sistema_solar):
        """
        Registra el estado del dia segun el estado del sistema solar
        Retorna el registro creado
        """
        if sistema_solar.planetas_alineados():
            if sistema_solar.sistema_alineado():
                self._agregar_dia_sequia(sistema_solar.dia)
            else:
                self._agregar_dia_optimo(sistema_solar.dia)
        elif sistema_solar.sol_encerrado():
            self._agregar_dia_lluvia(
                sistema_solar.dia,
                sistema_solar.distancia_entre_planetas())
        else:
            self._agregar_dia_normal(sistema_solar.dia)

        return self._registro[-1]
    
    def pronostico(self):
        periodos = dict(
            lluvia=0,
            sequia=0,
            optimo=0,
            normal=0,
            pico_lluvia=self._pico_lluvia['dia'] if self._pico_lluvia else 0)

        for estado, group_estados in itertools.groupby(sorted(self._registro, key=lambda e: e['estado']), lambda e: e['estado']):
            for _, group_periodos in itertools.groupby(enumerate(sorted(group_estados, key=lambda e: e['dia'])),
                                                       lambda x: x[0]-x[1]['dia']):
                if estado == Clima.CLIMAS['NORMAL']:
                    periodos['normal'] += len((list(map(itemgetter(1), group_periodos))))
                elif estado == Clima.CLIMAS['LLUVIA']:
                    periodos['lluvia'] += len((list(map(itemgetter(1), group_periodos))))
                elif estado == Clima.CLIMAS['SEQUIA']:
                    periodos['sequia'] += len((list(map(itemgetter(1), group_periodos))))
                elif estado == Clima.CLIMAS['OPTIMO']:
                    periodos['optimo'] += len((list(map(itemgetter(1), group_periodos))))

        return periodos
