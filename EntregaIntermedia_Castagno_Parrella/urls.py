
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('blog.urls')),
    path('appcomic/', include('appcomic.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, documento_root=settings.MEDIA_ROOT)