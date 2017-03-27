from django.conf.urls import url

from . import views
app_name = 'api'
urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<typesofDoctor_name>[-\w]+)/$', views.doctor_list, name='doctor_list'),
]