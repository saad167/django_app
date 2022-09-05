from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    #path('<int:id>/add', views.add, name='add'),
    path('excel', views.export_excel, name='export_excel'),
    path('dashboard', views.plot, name='dashboard'),
]
