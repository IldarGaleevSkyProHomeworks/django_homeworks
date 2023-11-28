from django.urls import path

from blog_app.apps import BlogAppConfig
from blog_app.views import ArticleListView, ArticleDetailView

app_name = BlogAppConfig.name

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]
