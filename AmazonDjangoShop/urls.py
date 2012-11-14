from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'shop.views.home', name='home'),
    url(r'^page/(?P<slug>[-\w]+)/$', 'shop.views.static_page', name='static page'),
    url(r'^category/(?P<node_id>[-\w]+)/$', 'shop.views.category_view', name='category'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
