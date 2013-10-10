from django.conf.urls import patterns, url
from finance_entries import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                       url(r'^$', login_required(views.IndexView.as_view()), name='index'),
                       url(r'^logout/$', views.logout_view, name='logout'),
                       url(r'^upload_file/$', views.upload_file, name='upload_file'),
                       url(r'^detail/(?P<pk>\d+)/$', views.DetailView.as_view(),
                           name='transaction_detail'),
                       url(r'^all/$', views.ListAllView.as_view(),
                           name='all_transactions'),
                       )
