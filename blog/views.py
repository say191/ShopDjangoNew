from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Blog
from pytils.translit import slugify
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'date_created')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'date_created')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.slug])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
