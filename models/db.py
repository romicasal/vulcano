# -*- coding: utf-8 -*-

db.define_table(
    'planeta',
    Field('nombre', 'string', notnull=True, unique=True),
    Field('distancia', 'integer', notnull=True, unique=True),
    Field('angulo', 'integer', notnull=True),
    Field('velocidad', 'integer', notnull=True),
    Field('sentido', 'integer', notnull=True)
)

db.define_table(
    'clima_registro',
    Field('dia', 'integer', notnull=True, unique=True),
    Field('clima', 'string', notnull=True)
)

db.define_table(
    'planeta_posicion',
    Field('dia', 'integer', notnull=True),
    Field('nombre', 'string', notnull=True),
    Field('rho', 'double', notnull=True),
    Field('phi', 'double', notnull=True)
)

db.define_table(
    'clima_estadistica',
    Field('clima', 'string', notnull=True),
    Field('valor', 'integer', notnull=True)
)
