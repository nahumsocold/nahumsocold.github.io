"""webEmpresarial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    #path de services
    path('services/', include('services.urls')),

    #path de core
    path('', include('core.urls')),

    #PATH BLOG
    path('blog/', include('blog.urls')),

    #PATH PAGES
    path('page/', include('pages.urls')),

    #PATH CONTACT
    path('contact/', include('contact.urls')),

    #PATH ADMIN
    path('admin/', admin.site.urls),
]

# MY FICHEROS MEDIAS: HACEMOS ESTO PARTA Q LOS ARCHIVOS MEDIAS SE PUEDAN MOSTAR EN LA PAGINA
if settings.DEBUG:
    from  django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)