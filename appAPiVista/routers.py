from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'facultades', FacultadViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'relacion_materias',Relacion_MateriaViewSet,basename='relacion_materias'),


urlpatterns = router.urls