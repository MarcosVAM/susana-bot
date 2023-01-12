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
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('grafico/', views.grafico, name="grafico"),
    path('api-auth/', include('rest_framework.urls')),
    #path("", views.uploadFile, name = "uploadFile"),
    path("teste/<int:v1>/<int:v2>/<int:v3>/<int:v4>", views.teste, name = "teste"),
    path("selecionar/", views.seleciona, name = "selecionar"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )