from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from posts.forms import CreatePostForm
from django.contrib.messages.views import SuccessMessageMixin
from posts.models import Post


# using as_view to call this class
class ListPostView(ListView):
    model = Post

    def get(self, request, *args, **kwargs):
        template_name = "posts/list-posts.html"
        obj = {"posts": Post.objects.all()}
        return render(request, template_name, obj)


class CreatePostView(SuccessMessageMixin, CreateView):
    template_name = "posts/create-post.html"
    form_class = CreatePostForm
    success_message = "Crate Post successfully!"


class UpdatePostView(SuccessMessageMixin, UpdateView):
    template_name = "posts/edit-post.html"
    model = Post
    fields = [
        "name",
        "content",
    ]
    success_message = "Update Post successfully!"

    def get_success_url(self):
        return reverse("posts:list-posts", kwargs={})
