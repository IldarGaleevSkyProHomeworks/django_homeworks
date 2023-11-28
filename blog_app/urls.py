from django.urls import path

from blog_app.apps import BlogAppConfig
from blog_app.views import ArticleListView

app_name = BlogAppConfig.name

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
]
