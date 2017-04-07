from django.conf.urls import include, url
from django.contrib import admin
from Modelado import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Curso2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Front/', include('Front.urls')),
    url(r'^registro/', include('Modelado.urls')),
    
]
