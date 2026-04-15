from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', add, name='add'),
    # complete page url
    path('complete/', complete, name='complete'), 
    path('trash/', trash, name='trash'),
    path('about/', about, name='about'),

    path('update/<int:id>', update, name='update'),#this is home page update botten
    path('complete_/<int:id>', complete_, name='complete_'), # this is home page complete button url
    path('delete_/<int:id>', delete_, name='delete_'), #home page delete button
    path('complete_all/', complete_all, name='complete_all'), # home page complete all button
    path('delete_all/', delete_all, name='delete_all'),

    path('c_restore/<int:id>/', c_restore, name='c_restore'), # complete page restore button
    path('c_restore_all/', c_restore_all, name='c_restore_all'),
    path('c_delete/<int:id>', c_delete, name='c_delete'),
    path('c_delete_all/', c_delete_all, name='c_delete_all'),


    path('t_delete/<int:id>', t_delete, name='t_delete'),
    path('t_delete_all/',t_delete_all, name='t_delete_all' )
]