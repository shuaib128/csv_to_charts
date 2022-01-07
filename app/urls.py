from django.urls import path
from .views import(
    home, multiple_chat_home
)


urlpatterns = [
    path('', home, name='homapage'),
    path('many', multiple_chat_home, name='multiple_chat_home')
]