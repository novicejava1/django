from django.urls import path

from . import views

urlpatterns = [
    path('barchart', views.myFirstChart, name='barchart'),
    path('tablechart', views.mySecondChart, name='tablechart'),
    path('piechart', views.myThirdChart, name='piechart'),
    path('linechart', views.myFourthChart, name='linechart'),
    path('myform', views.get_name, name='myform'),
    path('name', views.get_name, name='myform'),
    path('simpleupload', views.simple_upload, name='simpleupload'),
    path('selectchart', views.select_chart, name='selectchart'),
    path('chart', views.select_chart, name='selectchart'),
]

