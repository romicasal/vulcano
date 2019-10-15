# -*- coding: utf-8 -*-


def index():
    response.flash = ""
    estadisticas = db(db.clima_estadistica.id > 0).select()
    return dict(estadisticas=estadisticas)

def clima():
    return dict(grid=SQLFORM.grid(db.clima_registro, fields=[db.clima_registro.dia, db.clima_registro.clima],
                                  editable=False, deletable=False, searchable=True,
                                  create=False, details=False, csv=False))
def planetas():
    return dict(grid=SQLFORM.grid(db.planeta_posicion, fields=[db.planeta_posicion.dia, db.planeta_posicion.rho, db.planeta_posicion.phi],
                                  editable=False, deletable=False, searchable=True,
                                  create=False, details=False, csv=False))

def setup():
    limpiar_modelo()
    task_cargar_clima()
    redirect(URL('default', 'index'))