from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as roca
from . import views

urlpatterns = [
        url(r'^admin/$', admin.site.urls),
 	url(r'^$', views.inicio, name = "Inicio"),
 	url(r'^login/$', roca.login, name='Login'),
 	#url(r'^logout/$', roca.logout, name='Logout'),
	url(r'^registro/$', views.registro, name ="Registro"),
    ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
