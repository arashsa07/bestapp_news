from django.conf.urls import url
import views

urlpatterns = [
    url(r'^news_post/(?P<post_id>[0-9]+)/(?P<slug>[a-zA-Z0-9_-]+)/$', views.news_post, name="view_news_post"),
    url(r'^get_categories/(?P<agency_id>[0-9]+)/$', views.get_categories),
    url(r'^search_news/(?P<category_id>[0-9]+)/(?P<regex>\w+)/$', views.search_news),
    url(r'^get_news/(?P<agency_id>[0-9]+)/$', views.get_news),
]