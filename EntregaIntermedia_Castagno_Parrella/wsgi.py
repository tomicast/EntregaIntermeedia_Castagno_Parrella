

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EntregaIntermedia_Castagno_Parrella.settings')

application = get_wsgi_application()
