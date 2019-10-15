# -*- coding: utf-8 -*-

def clima():
    if not request.env.request_method == 'GET': raise HTTP(403)
    try:
        dia = request.vars.dia
        rec = db(db.clima_registro.dia == dia).select().last()
        if not rec:
            raise HTTP(404, 'No se encuentran datos para el dia solicitado')
    except ValueError:
        raise HTTP(404, 'El dia debe ser un numero entero')
    return response.json(dict(dia=rec.dia, clima=rec.clima.lower()))
