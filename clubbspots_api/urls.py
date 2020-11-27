"""clubbspots_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from api.views import ListClubs, DetailClubs, ListReports
from django.conf.urls import url
from api import urls
from . import views

urlpatterns = [
    path('toshikikai/aichisendou/', admin.site.urls),
    path('clublistasventures', ListClubs.as_view()),
    path('clublistasventures/<int:pk>/', DetailClubs.as_view()),
    url(r'^login/',views.login_view, name='login'),
    url(r'^logout/$', views.logout_view),
    path('', include('api.urls')),
    path('reportsforconsideration/', ListReports.as_view()),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

