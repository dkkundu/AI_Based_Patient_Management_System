from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    path('patient/', include('patient_ms.urls')),
    path('appointment/', include('appointment.urls')),

    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('django_prometheus.urls')),
    path('core/', include('Core.urls')),
    path('core/api/', include('API.urls')),
    path('api/', include('patient_ms.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
