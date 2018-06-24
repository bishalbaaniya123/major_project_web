from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^test$', views.home2),
    url(r'^data$', views.sendjson),
    url(r'^data2$', views.sendjson2),
    url(r'^start$', views.startfunction),
    url(r'^end$', views.endfunction),
]
