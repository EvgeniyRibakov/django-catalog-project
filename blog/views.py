from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog.models import Post


class BlogListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(was_publication=True)


class BlogDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Post
    fields = (
        "name",
        "description",
        "image",
        "created_at",
        "was_publication",
        "views_counter",
    )
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Post
    fields = (
        "name",
        "description",
        "image",
        "created_at",
        "was_publication",
        "views_counter",
    )
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:blog_list")
