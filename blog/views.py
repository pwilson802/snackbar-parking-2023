from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

def post_list(request):
    return render(request, 'blog/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

class PostListViewCategory(ListView):
    model = Post
    template_name = 'blog/categories.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        user_email = request.POST['emailaddress']
        email_body = f"sender: {user_email}\n\n{message}"
        mail_sent = send_mail('Website Contact Form', 
                    email_body, 
		            settings.EMAIL_HOST_USER,
		            ['contact@snackbarparking.com'], 
		            fail_silently=False)
        if mail_sent == True:
            messages.info(request, 'Thanks for the Feedback.')
    return render(request, 'blog/contact.html')