from django.urls import path
from .views import RegisterView, LoginView, BlogList, BlogDetail, MyBlogs, CommentList

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('my-blogs/', MyBlogs.as_view(), name='my-blogs'),
    path('blogs/<int:blog_pk>/comments/', CommentList.as_view(), name='comment-list'),
]
