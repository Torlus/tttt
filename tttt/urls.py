from django.conf.urls import url, include
# from django.conf.urls import patterns

# from api.views import UserList, UserDetail
# from api.views import GroupList, GroupDetail

from rest_framework.routers import DefaultRouter
from api import views

from django.contrib import admin
admin.autodiscover()

# user_urls = patterns(
#     '',
#     url(r'^/(?P<pk>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
#     url(r'^$', UserList.as_view(), name='user-list')
# )

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'works', views.WorkViewSet)
router.include_root_view = False

urlpatterns = [
    url(r'^$', views.APIRootView.as_view(), name='api-root'),
    url(r'^', include(router.urls)),
    # url(r'^users', include(user_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
