from django.urls import path

from .consumers import Chatconsumer

websocket_urlpatterns={
    path('ws/wsc/<str:room_name>/',Chatconsumer.as_asgi())
}