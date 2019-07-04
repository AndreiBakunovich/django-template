from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.view_point, name='view_point'),
    url(r'^search_point$', views.search_point, name='search_point'),
    url(r'^belarus-bible$', TemplateView.as_view(template_name='data_server/belarusandbible.html'), name='belarus-bible'),
    url(r'^tibo2019$', TemplateView.as_view(template_name='data_server/tibo2019.html'), name='tibo2019'),
    url(r'^biarescie$', TemplateView.as_view(template_name='data_server/biarescie.html'), name='biarescie')
]
