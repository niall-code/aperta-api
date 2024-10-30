from django.urls import path
from follows import views


urlpatterns = [
    path('followed/', views.FollowList.as_view()),
    path('followed/<int:pk>/', views.FollowDetail.as_view())
]
