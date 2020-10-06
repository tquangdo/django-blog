from django.urls import path
# ~~~ C1 ~~~
from . import views
# ~~~ C2 ~~~
from django.views.generic import ListView, DetailView
from .models import Post
from .views import AddPost

app_name = 'blog'
urlpatterns = [
    # ~~~ C1 ~~~
    # path('', views.onList, name='blog_dotq'),  #'...8000/blog_dotq/'
    # path('<int:arg_id>/', views.onPost,
    #      name='post_dotq'),

    # ~~~ C2 ~~~
    # as_view() là generic view
    path('',
         ListView.as_view(queryset=Post.objects.all().order_by('-date'),
                          template_name='pages/blog_dotq.html',
                          context_object_name='postOnList',
                          paginate_by=5),
         name='blog_dotq'),
    # ~~~ Lúc chưa có Comment ~~~
    #     path('<int:pk>/', #KO được là "arg_pk" hay name khác!!! (vì "pk" ko được gọi ở đâu nữa)
    #          DetailView.as_view(model=Post,
    #                             template_name='pages/post_dotq.html',
    #                             context_object_name='postOnPost'),
    #          name='post_dotq')
    # ~~~ Lúc đã có Comment (giống C1) ~~~
    path('<int:arg_pk>/', views.onPost, name='post_dotq'),
    path(
        '<int:arg_pk>/vote_result/', views.onVote, name='vote_dotq'
    ),  #'<int:arg_pk>' được truyền từ 'postOnPost.id' of file "post_dotq.html" với mapping:'blog:vote_dotq'
    path('add-post/', AddPost.as_view(), name='them_post')
]
