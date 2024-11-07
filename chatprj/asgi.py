"""
ASGI config for chatprj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import URLRouter,ProtocolTypeRouter
from Chatapp import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatprj.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        routing.websocket_urlpatterns
    )
})
