"""
URL configuration for homeless_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf.urls.static import static
from residents import views


urlpatterns = [
    path("healthz/", views.healthz, name="heamthz"),
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("residents/", views.resident_list, name="residents_list"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path("residents/<int:resident_id>/", views.resident_detail, name="resident_detail"),
    path("residents/<int:resident_id>/edit/", views.resident_edit, name="resident_edit"),
    path("residents/create/", views.resident_create, name="resident_create"),
    path("residents/<int:resident_id>/delete/", views.resident_delete, name="resident_delete"),
]

if  settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
