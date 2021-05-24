from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings as sett
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include("base.urls")),
] 
if settings.DEBUG == True:
    urlpatterns += static(sett.MEDIA_URL, document_root=sett.MEDIA_ROOT)

handler400 = 'base.views.error_400'
handler403 = 'base.views.error_403'
handler404 = 'base.views.error_404'
handler503 = 'base.views.error_503'