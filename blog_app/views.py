from django.db.models import Q
from django.views.generic import ListView, DetailView

from blog_app.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_published=True).order_by('-create_date')

        return qs


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
