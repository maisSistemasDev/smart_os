
from django.urls import include, re_path, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('authentication.urls')),
    path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),
    path('api/', include('core.urls')),
]
