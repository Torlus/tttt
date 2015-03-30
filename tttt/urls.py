from django.conf.urls import patterns, url, include
from tttt.api.views import UserList, UserDetail, UserViewSet
from tttt.api.views import GroupList, GroupDetail, GroupViewSet
from rest_framework import routers
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

user_urls = patterns(
    '',
    url(r'^/(?P<pk>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
)

group_urls = patterns(
    '',
    url(r'^/(?P<pk>[0-9a-zA-Z_-]+)$', GroupDetail.as_view(), name='group-detail'),
    url(r'^$', GroupList.as_view(), name='group-list')
)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', include(router.urls)),
    url(r'^users', include(user_urls)),
    url(r'^groups', include(group_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
