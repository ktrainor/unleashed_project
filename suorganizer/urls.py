from django.conf.urls import include, url
from django.contrib import admin

from .views import redirect_root

from organizer import urls as organizer_urls
from blog import urls as blog_urls

urlpatterns = [
    url(r'^$', redirect_root),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(organizer_urls)),
    url(r'^blog/', include(blog_urls)),
]
