"""AmazonDjangoShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from shop import views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', app_views.home, name='home'),
    url(r'^(?P<cat_slug>[-\w]+)/(?P<asin>[-\w]{10})/$', app_views.product_page, name='product_page'),
    url(r'^(?P<slug>[-\w]+)/$', app_views.category_view, name='category_view'),
    url(r'^page/(?P<slug>[-\w]+)/$', app_views.static_page, name='static_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
