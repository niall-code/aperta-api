from django.urls import path
from reports import views


urlpatterns = [
    path('suspicious/', views.SuspiciousList.as_view()),
    path('suspicious/<int:post_id>/', views.SuspiciousList.as_view()),
    path('suspicious/<int:pk>/', views.SuspiciousDetail.as_view()),
]
