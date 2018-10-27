from django.conf.urls import url
from .views import news_post, get_categories, search_news, get_news

urlpatterns = [
    url(r'^news_post/(?P<post_id>[0-9]+)/(?P<slug>[a-zA-Z0-9_-]+)/$', news_post, name="view_news_post"),
    url(r'^get_categories/(?P<agency_id>[0-9]+)/$', get_categories),
    url(r'^search_news/(?P<category_id>[0-9]+)/(?P<regex>\w+)/$', search_news),
    url(r'^get_news/(?P<agency_id>[0-9]+)/$', get_news),
]
