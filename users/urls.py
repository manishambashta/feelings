from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [

    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url('^', include('django.contrib.auth.urls')),
]