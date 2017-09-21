from django.conf.urls import url

from . import views

app_name = 'django_assist'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<step_id>[0-9]+)/run_step/$', views.run_step, name='run_step'),
]