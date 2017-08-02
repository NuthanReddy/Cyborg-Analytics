from django.conf.urls import url
from . import views

app_name = 'mlearn'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^(?P<dataset_id>[0-9]+)/$', views.show_dataset, name='show_dataset'),
    url(r'^add_dataset/$', views.create_dataset, name='create_dataset'),
    url(r'^(?P<dataset_id>[0-9]+)/delete_dataset/$', views.delete_dataset, name='delete_dataset'),
]
