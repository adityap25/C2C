from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostListView.as_view(),name='hiring-home'),
    path('user/<str:username>/', UserPostListView.as_view(),name='hiring-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='hiring-detail'),
    path('post/new/', PostCreateView.as_view(),name='hiring-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='hiring-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='hiring-delete'),
    path('about/', views.about,name='about'),
    path('search/', views.search_job,name='search-job'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
