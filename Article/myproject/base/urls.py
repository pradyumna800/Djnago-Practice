from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/', news, name='news'),
    path('events/', events, name='events'),
    path('about/', about, name='about'),
    path('read/<int:id>', read, name='read'),
    path('news_show/<int:id>', n_news, name='news_show')
]