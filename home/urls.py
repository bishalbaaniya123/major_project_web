from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^data$', views.sendjson),
    url(r'^start$', views.startfunction),
    url(r'^end$', views.endfunction),
    url(r'^checkServer$', views.checkServer),
    url(r'^checkServerStatus$', views.checkServerStatus),
    url(r'^checkIdle$', views.checkIdle),
    url(r'^get_flows$', views.get_flows),
]
