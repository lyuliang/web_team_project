from django.urls import path,include
import grumblr.views
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', grumblr.views.home),
    path('login/', grumblr.views.log),
    path('register/', grumblr.views.register),
    path('share/', grumblr.views.share),
    path('global/', grumblr.views.glo),
    path('mypro/', grumblr.views.mypro),
    path('epro/', grumblr.views.edit),
    path('mypro/#', grumblr.views.mypro),
    path('logout/', grumblr.views.out),
    path('pro/', grumblr.views.pro),
    path('follow/', grumblr.views.follow),
    path('verify/', grumblr.views.verify),
    path('reset/', grumblr.views.reset),
    path('reset2/', grumblr.views.forget),
    path('forget/', grumblr.views.forget),
    path('reset_password/', grumblr.views.reset_password),
    path('reset_password2/', grumblr.views.reset_pass2),
    path(r'^<username><token>', grumblr.views.confirm, name='confirm'),
    path(r'^<first_name><token>', grumblr.views.reset, name='reset'),
    path(r'^<username><first_name><token>', grumblr.views.forget, name='re'),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
