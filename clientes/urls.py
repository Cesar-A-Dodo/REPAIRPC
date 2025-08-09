from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('atualiza_cliente/', views.att_cliente, name="atualiza_cliente"),
    path('update_maquina/<int:id>', views.update_maquina, name="update_maquina"),
    path('excluir_maquina/<int:id>', views.excluir_maquina, name="excluir_maquina")
]