from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'facultades', FacultadViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'materias', MateriaViewSet)


urlpatterns = router.urls