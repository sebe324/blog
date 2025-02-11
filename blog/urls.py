from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name="blog"


urlpatterns = [
    path('',views.blog_index,name='index'),
    # path('category/<str:category>',views.blog_category, name='category'),
    path('post/<int:pk>/',views.blog_post,name='post'),
    path('posts/',views.blog_allposts,name="posts"),
    path('projects/',views.blog_allprojects,name="projects"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
