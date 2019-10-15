'''
Created on Oct 6, 2019

@author: romina
'''

"""
Programa para probar graficamente los resultados
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from utiles.point import PolarPoint
from planeta import Planeta
from sistema_solar import SistemaSolar

INTERVALO = 90
FRAMES = 360
GIF = False

phiv = 0        
phif = 0
phib = 0

vulcanos = Planeta("Vulcanos", phiv, 500, 1, -1)
ferengis = Planeta("Ferengis", phif, 2000, 3, -1)
betasoides = Planeta("Betasoides", phib, 1000, 5, 1)

sistema = SistemaSolar(planetas=(vulcanos, ferengis, betasoides), dia=0)

circle0 = plt.Circle((0, 0), 200, color='yellow', fill=True)
circle1 = plt.Circle((0, 0), vulcanos.pos.rho, color='r', fill=False)
circle2 = plt.Circle((0, 0), ferengis.pos.rho, color='g', fill=False)
circle3 = plt.Circle((0, 0), betasoides.pos.rho, color='b', fill=False)

fig, ax = plt.subplots()

plt.xlim(-2250,2250)
plt.ylim(-2250,2250)

plt.grid(linestyle='--')

ax.set_aspect(1)

ax.add_artist(circle0)
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)


pos1 = PolarPoint.pol2cart(vulcanos.pos)
pos2 = PolarPoint.pol2cart(ferengis.pos)
pos3 = PolarPoint.pol2cart(betasoides.pos)

p1, = plt.plot([], [], 'ro')
p2, = plt.plot([], [], 'go')
p3, = plt.plot([], [], 'bo')

an1 = ax.annotate(vulcanos.nombre, pos1.xy)
an2 = ax.annotate(ferengis.nombre, pos2.xy)
an3 = ax.annotate(betasoides.nombre, pos3.xy)

l12, = plt.plot([], [], 'k-')
l23, = plt.plot([], [], 'k-')
l31, = plt.plot([], [], 'k-')

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
desc = ax.text(0.05, 0.95, "Dia: \nClima: ", transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.title('Sistema Solar', fontsize=8)

def init():
    return p1,p2,p3
 
def animate(_):
    data = sistema.do_step()
 
    pos1 = PolarPoint.pol2cart(vulcanos.pos)
    pos2 = PolarPoint.pol2cart(ferengis.pos)
    pos3 = PolarPoint.pol2cart(betasoides.pos)
     
    p1.set_data(*pos1.xy)
    p2.set_data(*pos2.xy)
    p3.set_data(*pos3.xy)
     
    an1.set_position(pos1.xy)
    an2.set_position(pos2.xy)
    an3.set_position(pos3.xy)
 
    l12.set_data([pos1.x,pos2.x],[pos1.y,pos2.y])
    l23.set_data([pos2.x,pos3.x],[pos2.y,pos3.y])
    l31.set_data([pos3.x,pos1.x],[pos3.y,pos1.y])
    
    desc.set_text("Dia: %s\nClima: %s" % (data['dia'], data['estado']))

    return p1,p2,p3
 
ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=INTERVALO, frames=FRAMES, repeat=False)
 
if GIF:
    ani.save('animation.gif', writer='imagemagick', fps=30)

plt.show()

print(sistema.pronostico_clima())