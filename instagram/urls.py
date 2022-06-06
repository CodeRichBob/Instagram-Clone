from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('' , views.post, name='post'),
    path('profile/' , views.profile, name='profile'),
    path('<int:post_id>/like',views.like, name = 'postlike'),
    path('comments/<int:pk>' , views.new_comment, name='comment'),
    path('new/' , views.new_post, name='new-post'),
    path('search/', views.search_results, name ='search_results'),
    path('delete/<int:pk>',views.delete_post, name = 'deletepost'), 
    path('update/<str:pk>',views.update_post, name = 'updatepost'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)