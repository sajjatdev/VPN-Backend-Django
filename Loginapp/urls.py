from django.urls import path
from .views import Login, logout_view

app_name = 'Auth'

urlpatterns = [
    path('login/', Login, name="login"),
    path('logout/', logout_view, name='logout')
]
