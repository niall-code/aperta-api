from django.contrib import admin
from django.urls import path, include

from .views import root_route, logout_route


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('follows.urls')),
    path('', include('blocks.urls')),
    path('', include('reports.urls')),
    path('', include('approvals.urls')),
    path('', root_route),
]
