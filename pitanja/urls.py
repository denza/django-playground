from django.conf.urls import url
from pitanja import views
from django.urls import path, include

urlpatterns = [
    url(r'^$', views.poosobama, name = 'PoOsobama'),
]
