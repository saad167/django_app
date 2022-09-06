from django.urls import path

from . import views

from . import plot
urlpatterns = [
    path('', views.index,name="index"),
    #path('<int:id>/add', views.add, name='add'),
    path('excel', views.export_excel, name='export_excel'),
    path('dash', views.plot, name='dashboard'),
]
