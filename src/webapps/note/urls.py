from django.urls import path,include
import note.views
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('register/',note.views.register,name = 'register'),
    path('login/',note.views.logIn,name = 'login'),
    path('index/',note.views.index,name = 'index'),
    path('course/',note.views.course,name = 'course'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
