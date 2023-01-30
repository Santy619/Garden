from django.urls import path
from rest_planta.views import lista_plantas, detalle_planta
from rest_planta.viewslogin import login

urlpatterns = [
    path('lista_plantas', lista_plantas, name="lista_plantas"),
    path('detalle_planta/<id>', detalle_planta, name="detalle_planta"),
    path('login', login, name="login"),
]