from django.urls import path
from .views import(
    Home, multiple_chat_home
)


urlpatterns = [
    path('', Home.as_view(), name='homapage'),
    path('many', multiple_chat_home.as_view(), name='multiple_chat_home')
]