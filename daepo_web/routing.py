from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from daepo_app.consumer import Consumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/", Consumer)
    ]),
})
