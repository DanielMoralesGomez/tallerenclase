from rest_framework.routers import DefaultRouter
from ..autor.views import *
from ..genero.views import *
from ..libro.views import *


router = DefaultRouter()

router.register(r'autor', AutorViewSet, basename='Autor')
router.register(r'genero', GeneroViewSet, basename='Genero')
router.register(r'libro', LibroViewSet, basename='Libro')


urlpatterns = router.urls