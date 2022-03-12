from django.shortcuts import get_object_or_404, redirect, render,get_object_or_404
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin,PermissionRequiredMixin
from django.contrib import messages
from users.models import User
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='blog/home.html' 
    context_object_name='posts' 
    ordering=['-date_posted']
    # paginate_by=5

class UserPostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts' 
    # paginate_by=5
    
    def get_queryset(self):
        user=get_object_or_404(User,email=self.kwargs.get('email'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model=Post
    fields=['domain','role','skills','opening','location','last_date','jd']
    success_message='Hiring Created Successfully'
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def has_permission(self):
        return self.request.user.type=="Company"

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model=Post
    fields=['domain','role','skills','opening','location','last_date','jd']
    success_message='Hiring Updated Successfully'
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        return self.request.user==post.author

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model=Post
    success_message='Hiring Deleted Successfully'
    success_url='/'
    def test_func(self):
        post=self.get_object()
        return self.request.user==post.author
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

@login_required
def about(request):
    return render(request,'blog/about.html')

@login_required
def search_job(request):
    return render(request,'blog/search_job.html')