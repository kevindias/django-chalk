from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .feeds import ArticleAtomFeed, ArticleRssFeed
from .views import ArticleView, ArticleList


urlpatterns = patterns('',
    url(r'^$', ArticleList.as_view(), name='list_articles'),
    url(r'^feed/$', TemplateView.as_view(template_name='chalk/feed_list.html'),
        name='list_feeds'),
    url(r'^feed/rss/$', ArticleRssFeed(), name='rss_feed'),
    url(r'^feed/atom/$', ArticleAtomFeed(), name='atom_feed'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleView.as_view(), name='view_article'),
)
