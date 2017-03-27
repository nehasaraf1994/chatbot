from django.conf.urls import url

from . import views
app_name = 'testing'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<typesofDoctor_name>[-\w]+)/$', views.detail, name='detail'),
]