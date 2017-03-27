from django.conf.urls import url

from . import views
app_name = 'webhookExmp'
urlpatterns = [
    url(r'^$', views.hook_list, name='hook_list'),
    #url(r'^(?P<typesofDoctor_name>[-\w]+)/$', views.doctor_list, name='doctor_list'),
]