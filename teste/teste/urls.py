from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views
from django.conf import settings
from django.conf.urls.static import static

#router = routers.DefaultRouter()
#router.register()

app_name = "Core"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grafico/', views.grafico, name="grafico"),
]

