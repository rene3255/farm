from xml.dom.minidom import Document
from django.urls import path
from . import views
app_name = 'farm_app'
urlpatterns= [
  path('', views.rabbit_list, name='rabbit_list'),
  
]

