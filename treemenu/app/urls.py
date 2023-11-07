from django.urls import path

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('<slug>/', home, name='sub'),
    path('<slug>/<path>/', home, name='doublesub')
]
