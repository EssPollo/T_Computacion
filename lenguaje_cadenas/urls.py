
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OperacionesViewSet 

# Crear un router y registrar el ViewSet
router = DefaultRouter()
router.register(r'operaciones', OperacionesViewSet, basename='operaciones')

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas generadas por el router
    #path('users/<uuid:id>/', UsuarioViewSet.as_view({'put': 'update'}), name='actualizar-usuario-completo'),
]
