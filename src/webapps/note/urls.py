from django.urls import path,include
import note.views
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
