'''
Created on Oct 9, 2019

@author: romina
'''

"""
Programa para probar el pronostico
"""

from planeta import Planeta
from sistema_solar import SistemaSolar

phiv = 0        
phif = 0
phib = 0

vulcanos = Planeta("Vulcanos", phiv, 500, 1, -1)
ferengis = Planeta("Ferengis", phif, 2000, 3, -1)
betasoides = Planeta("Betasoides", phib, 1000, 5, 1)

sistema = SistemaSolar(planetas=(vulcanos, ferengis, betasoides), dia=0)

for _ in range(0, 360*10): # 360 es la cantidad de dias del planeta que mas tarda en dar una vuelta
    sistema.do_step()

print(sistema.pronostico_clima())
