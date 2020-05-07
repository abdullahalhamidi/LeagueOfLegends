from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from champions.views import champions
from homepage.views import homepage
from items.views import items



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', homepage),
    url(r'^champions/$', champions),
    url(r'^items/$', items),
]
