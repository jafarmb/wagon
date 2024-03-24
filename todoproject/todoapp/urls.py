from django.contrib import admin
from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/',views.update, name='update')

]





