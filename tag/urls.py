from django.conf.urls import url
from . import views

app_name = 'tag'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
]
