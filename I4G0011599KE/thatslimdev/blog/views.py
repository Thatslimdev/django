
from django.views import generic
from django.urls import reverse_lazy

from blog.models import Post


class PostListViews(generic.ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('blog:all')

class PostCreateViews(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDetailViews(generic.DetailView):
    model = Post   

class PostUpdateViews(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteViews(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")    
# Create your views here.
