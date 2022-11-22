
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('sports/',views.sports,name='sports'),
    path('science/',views.science,name='science'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('business/',views.business,name='business'),
]