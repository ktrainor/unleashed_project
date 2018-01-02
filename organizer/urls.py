from django.conf.urls import url

from .views import (startup_list, startup_detail,
                    tag_detail, tag_list, tag_create)

urlpatterns = [
    url(r'^startup/$',
        startup_list,
        name='organizer_startup_list'),
    url(r'^startup/(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),
    url(r'^tag/$',
        tag_list,
        name = 'organizer_tag_list'),
    url(r'^tag/create/$',
        tag_create,
        name='organizer_tag_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'),
]
