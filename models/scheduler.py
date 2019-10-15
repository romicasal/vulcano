# -*- coding: utf-8 -*-

import datetime
from sistema_solar import SistemaSolar
from planeta import Planeta

VUELTA_AL_SOL = 360 # grados (deg)
ANIOS_PRONOSTICO = 10

def limpiar_modelo():
    db.planeta.truncate()
    db.planeta_posicion.truncate()
    db.clima_registro.truncate()
    db.clima_estadistica.truncate()

def cargar_planetas():
    if not db(db.planeta.id > 0).count():
        db.planeta.insert(nombre='Vulcanos', distancia=500, angulo=0, velocidad=1, sentido=-1)
        db.planeta.insert(nombre='Ferengis', distancia=2000, angulo=0, velocidad=3, sentido=-1)
        db.planeta.insert(nombre='Betasoides', distancia=1000, angulo=0, velocidad=5, sentido=1)
    return db(db.planeta.id > 0).select()

def cargar_data(dia_inicio):
    planetas = []
    for record in cargar_planetas():
        planetas.append(Planeta(record.nombre, record.angulo, record.distancia, record.velocidad, record.sentido))

    sistema = SistemaSolar(planetas=planetas, dia=dia_inicio)
    
    min_vel = db.planeta.velocidad.min()
    min_vel = db(db.planeta.id > 0).select(min_vel).first()[min_vel]
    
    diasporanio = VUELTA_AL_SOL // min_vel
    
    for i in range(0, diasporanio * ANIOS_PRONOSTICO):
        data = sistema.do_step()
        db.clima_registro.insert(dia=data['dia'], clima=data['estado'])
        for planeta in sistema.planetas:
            db.planeta_posicion.insert(dia=sistema.dia, **planeta.__dict__())
        
    
    pronostico = sistema.pronostico_clima()
    db.clima_estadistica.truncate()
    for k, v in pronostico.items():
        db.clima_estadistica.insert(clima=k, valor=v)

def task_cargar_clima():
    """
    Se supone que esto funciona en un planeta del sistema solar donde los anios tienen 360 dias
    
    Si no hay pronosticos cargados o el dia actual es mayor o igual al max dia pronosticado
        entonces corro el script desde el ultimo dia registrado
    """
    max_dia = db.clima_registro.dia.max()
    max_dia = db(db.clima_registro.id > 0).select(max_dia).first()[max_dia]
    if not max_dia or max_dia >= datetime.datetime.now().day:
        cargar_data(max_dia or 0)
        return "Datos cargados"
    return "No se hace nada, ya existen datos para %s años" % ANIOS_PRONOSTICO
