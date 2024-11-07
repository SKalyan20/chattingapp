from django.urls import path
from .import views

urlpatterns = [
    path('',views.createroom,name='create-room'),
    path('<str:room_name>/<str:username>/',views.messageview,name='room'),
]
