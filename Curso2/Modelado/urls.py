'''
Created on 17/03/2017

@author: ave
'''

from django.conf.urls import include, url
from django.contrib import admin
from Modelado import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Curso2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.VistaMostrarRestaurantes, name='Vista Mostrar'),
    
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()