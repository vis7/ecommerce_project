from django.urls import path
from .views import registration, login, logout, user_list

app_name = 'accounts'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('user_list/', user_list, name='user_list'),
]
