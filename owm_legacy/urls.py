from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_config/(?P<key>[^/^.]+).md5$',
        views.get_config_md5,
        name='get_config_md5'),
    url(r'^get_config/(?P<key>[^/^.]+)$',
        views.get_config,
        name='get_config'),
]
