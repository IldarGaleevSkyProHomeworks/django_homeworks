from django.views.generic import ListView

from blog_app.models import Article


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_published=True).order_by('-create_date')

        return qs

