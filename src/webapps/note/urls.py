from django.urls import path,include
import note.views
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('register/',note.views.register,name = 'register'),
    path('login/',note.views.logIn,name = 'login'),
    path('logout/',note.views.logOut,name = 'logout'),
    path('index/<str:identity>',note.views.index,name = 'index'),
    path('course/<int:course_id>/',note.views.course,name = 'course'),
    path('create_course/',note.views.create_course,name = 'create_course'),
    path('join_course/',note.views.join_course,name = 'join_course'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
