
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('rabbit/list', include('farm_app.urls', namespace='farm_app')),
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     
