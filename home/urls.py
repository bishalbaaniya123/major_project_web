from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^data$', views.sendjson),
    url(r'^start$', views.startfunction),
    url(r'^end$', views.endfunction),
]
