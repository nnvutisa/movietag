from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[\w\-]+)/$', views.movierec, name='movie_rec'),
]
