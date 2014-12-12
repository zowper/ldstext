from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^api/', include('masstext.urls', namespace="masstext")),
    url(r'^admin/', include('masstext.urls', namespace="masstext")),
    url(r'^django/', include(admin.site.urls)),
)