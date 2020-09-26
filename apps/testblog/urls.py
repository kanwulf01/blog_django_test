from django.urls import path
from .views import home, general, tecnologia, programacion, videojuegos, tutoriales, signup

urlpatterns = [
    path('', home, name="index"),
    path('general/', general, name='general'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('programacion/', programacion, name='programacion'),
    path('videojuegos/', videojuegos, name='videojuegos'),
    path('tutoriales/', tutoriales, name='tutoriales'),
    path('signup/', signup, name='signup'),

]