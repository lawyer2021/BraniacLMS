import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('mainapp.urls')),
    path("", RedirectView.as_view(url="mainapp/")),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
    path("social_auth/", include("social_django.urls", namespace="social")),
    path("authapp/", include("authapp.urls", namespace="authapp")),
    path("i18n/", include("django.conf.urls.i18n")),

]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
