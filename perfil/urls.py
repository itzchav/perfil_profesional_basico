from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('publicaciones/', views.publicaciones, name='publicaciones'),  # si ya la tienes
    path('tesis/', views.tesis, name='tesis'),  # si ya la tienes
    


]
