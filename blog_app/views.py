from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog_app.apps import BlogAppConfig
from blog_app.models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = BlogAppConfig.articles_per_page

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_published=True).order_by('-create_date')

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Новые публикации'

        return ctx


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.object.title
        ctx['popular'] = Article.objects.filter(is_published=True).filter(~Q(id=self.object.id)).order_by('-view_count')[:3]
        return ctx

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'content_text', 'preview_image', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_obj = form.save()
            return redirect(reverse('blog_app:article_detail', kwargs={'slug': new_obj.slug}))


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'content_text', 'preview_image', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_obj = form.save()
            return redirect(reverse('blog_app:article_detail', kwargs={'slug': new_obj.slug}))


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog_app:articles')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = f'Удаление "{self.object.title}"'
        return ctx
