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
    path('course/<int:course_id>/<str:identity>/',note.views.course,name = 'course'),
    path('create_course/',note.views.create_course,name = 'create_course'),
    path('join_course/',note.views.join_course,name = 'join_course'),
    path('upload_file/', note.views.upload_file, name = 'upload_file'),
    # path('create_note/', note.views.create_note, name = 'create_note'),
    path('create_note/<str:course_number>/<str:identity>', note.views.create_note, name = 'create_note'),
    path('all_courses/<str:identity>', note.views.all_courses, name = 'all_courses'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('upload_note/', note.views.upload_note, name = 'upload_note'),
    path('dropdown_courselist/', note.views.dropdown_courselist, name='dropdown_courselist'),
    path('save_course/<str:identity>', note.views.save_choice, name = 'save_choice'),
    path('get_textnote/<int:note_id>', note.views.get_text_note, name = 'get_text_note'),
    path('get_pdf/<int:note_id>', note.views.get_pdf, name = 'get_pdf'),
    path('show_pdf/', note.views.show_pdf, name = 'show_pdf'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
