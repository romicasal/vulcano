# -*- coding: utf-8 -*-

from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires web2py 2.15.5 or newer")

configuration = AppConfig(reload=True)

db = DAL(configuration.get('db.uri'),
         pool_size=configuration.get('db.pool_size'),
         migrate_enabled=configuration.get('db.migrate'),
         check_reserved=['all'])

response.generic_patterns = [] 
if request.is_local and not configuration.get('app.production'):
    response.generic_patterns.append('*')

response.formstyle = 'bootstrap4_inline'
response.form_label_separator = ''

# auth = Auth(db, host_names=configuration.get('host.names'))
# auth.settings.extra_fields['auth_user'] = []
# auth.define_tables(username=False, signature=False)

# auth.settings.registration_requires_verification = False
# auth.settings.registration_requires_approval = False
# auth.settings.reset_password_requires_verification = True

response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.get('app.keywords')
response.meta.generator = configuration.get('app.generator')
response.show_toolbar = configuration.get('app.toolbar')

if configuration.get('scheduler.enabled'):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get('scheduler.heartbeat'), migrate=False)
