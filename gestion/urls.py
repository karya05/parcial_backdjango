from django.urls import path
from .views import ProjectEndpoint

urlpatterns = [
    path('proyectos/', ProjectEndpoint.as_view(), name='proyectos'),
    path('proyectos/<int:pk>/', ProjectEndpoint.as_view(), name='proyecto_detalle'),
]
