from django.urls import path

from . import views

'''
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
'''

urlpatterns = [
    path('', views.index, name='index'),
    path('2018/', views.special_case_2018, name='special_case_2003'),
    path('<int:year>/', views.get_year, name='get_year'),
]
