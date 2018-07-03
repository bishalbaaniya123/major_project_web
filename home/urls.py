from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^dateRange$', views.dateRange),
    url(r'^data$', views.sendjson),
    url(r'^start$', views.startfunction),
    url(r'^end$', views.endfunction),
    url(r'^checkServer$', views.checkServer),
    url(r'^checkServerStatus$', views.checkServerStatus),
    url(r'^checkIdle$', views.checkIdle),
    url(r'^get_flows$', views.get_flows),
    url(r'^not_count$', views.not_count),
    url(r'^get_flows_page1', views.get_flows_page1),
    url(r'^get_flows_page2', views.get_flows_page2),
    url(r'^send_command_service$', views.send_command_service),
]
