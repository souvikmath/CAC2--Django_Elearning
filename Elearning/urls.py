"""
URL configuration for Elearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static

=======
from teachers.views import *
>>>>>>> e730e2dd439303c2d33eaf1a3007597258db5044

admin.site.site_header = "Elearning Admin"
admin.site.site_title = "Elearning Admin Portal"
admin.site.index_title = "Welcome to Elearning Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('NumCrack.urls')),
<<<<<<< HEAD
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('login',login,name='login'),
    path('', include('authentication.urls')),
    path('halo',include('quizes.urls'),name='quizes'),
=======
    path('teachers/', include('teachers.urls')),
>>>>>>> e730e2dd439303c2d33eaf1a3007597258db5044
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)