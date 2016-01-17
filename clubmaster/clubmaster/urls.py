from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'clubmaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^attendance/', include('attendance.urls', namespace="attendance")),
    url(r'^', include('homepage.urls', namespace="homepage")),
    url(r'^admin/', include(admin.site.urls)),
]
