from django.conf.urls import patterns, url

from .views import ArticleView, ArticleList


urlpatterns = patterns('',
    url(r'^$', ArticleList.as_view(), name='list_articles'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleView.as_view(), name='view_article'),
)
