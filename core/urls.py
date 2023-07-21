from django.urls import path
from .views import *

urlpatterns = [
        path('', login, name='login'),
        path('home/', home, name='home'),
        path('valida_login/', valida_login, name='valida_login'),
        path('logout/', logout, name='logout'),
        path('adicionar_pedido/', adicionar_pedido, name = 'adicionar_pedido'),
        path('pedidos/', pedidos, name='pedidos'),
        path('update_pedido/<int:pk>', update_pedido, name='update_pedido'),
        path('apagar_pedido/<int:pk>', apagar_pedido, name="apagar_pedido"),

        ]
