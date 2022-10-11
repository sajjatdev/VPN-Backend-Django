from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Loginapp import urls as AuthUrl
from Dashboard import urls as DashUrl
from Dashboard import APiUrls as DashApiurl
urlpatterns = [

    path('dj-admin/', admin.site.urls),
    path('', include(AuthUrl), name="Auth"),
    path('', include(DashUrl), name="Dashboard"),
    path('api/v1/', include(DashApiurl), name="DashboardAPI")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
