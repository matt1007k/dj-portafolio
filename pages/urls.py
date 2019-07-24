from django.urls import path
from .views import Home
app_name = 'pages'
urlpatterns = [
    path('', Home, name='index')
]
