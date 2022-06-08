# from django.urls import path 
from django.urls import re_path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path('' , views.post, name='post'),
    re_path('profile/' , views.profile, name='profile'),
    re_path('<int:post_id>/like',views.like, name = 'postlike'),
    re_path('comments/<int:pk>' , views.new_comment, name='comment'),
    re_path('new/' , views.new_post, name='new-post'),
    re_path('search/', views.search_results, name ='search_results'),
    re_path('delete/<int:pk>',views.delete_post, name = 'deletepost'), 
    re_path('update/<str:pk>',views.update_post, name = 'updatepost'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)