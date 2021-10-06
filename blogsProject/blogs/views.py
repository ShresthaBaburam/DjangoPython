from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post

# Create your views here.

class BlogsHomePageView(ListView):
    model= Post
    template_name='home.html'
    context_object_name='all_posts_list'



class BlogsCreatePageView(CreateView):
    model= Post
    template_name='post_new.html'
    fields='__all__'

class BlogsDetailPageView(DetailView):
    model =Post
    template_name='post_deails.html'
    

class BlogsUpdatePageView(UpdateView):
    model= Post
    template_name='post_edit.html'
    fields='__all__'

class BlogsDeletePageView(DeleteView):
    model= Post
    template_name='post_remove.html'
    success_url=reverse_lazy('home')
    