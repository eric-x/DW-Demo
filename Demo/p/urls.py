from django.conf.urls import patterns, url

from p import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^(?P<store_id>\d+)/$', views.all_aps, name='all_aps'),
                        url(r'^(?P<store_id>\d+)/(?P<ap_nick>\w+)$', views.ap_status, name='ap_status'),
                        url(r'^(?P<store_id>\d+)/(?P<ap_nick>\w+)/(?P<status>\d+)$', views.update_ap_status, name='update_ap_status'),
)
