from django.urls import path

from blog_app.apps import BlogAppConfig
from blog_app.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogAppConfig.name

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<slug:slug>/edit', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<slug:slug>/delete', ArticleDeleteView.as_view(), name='article_delete'),
]
