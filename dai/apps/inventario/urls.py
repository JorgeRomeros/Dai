from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
	url(r'^$',IndexView.as_view(), name='index'),
	url(r'^homeindex/',HomeIndex.as_view(), name='homeindex'),
	url(r'^marca/',MarcaIndex.as_view(), name='marca'),
	url(r'^marcaadd/',MarcaAdd.as_view(), name='marcaadd'),
	url(r'^marcaupdate/(?P<pk>\d+)/$',MarcaUpdate.as_view(), name='marcaupdate'),
	url(r'^marcadelete/(?P<pk>\d+)/$',MarcaDelete.as_view(), name='marcadelete'),
	url(r'^modelo/',ModeloIndex.as_view(), name='modelo'),
	url(r'^modeloadd/',ModeloAdd.as_view(), name='modeloadd'),
	url(r'^modeloupdate/(?P<pk>\d+)/$',ModeloUpdate.as_view(), name='modeloupdate'),
	url(r'^modelodelete/(?P<pk>\d+)/$',ModeloDelete.as_view(), name='modelodelete'),
]
