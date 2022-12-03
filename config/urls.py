from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('mainapp.urls')),
    path("", RedirectView.as_view(url="mainapp/")),
    path('mainapp/', include('mainapp.urls', namespace='mainapp')),
]