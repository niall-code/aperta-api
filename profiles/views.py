from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from aperta_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    Lists all profiles. Provides filterset_fields,
    required by front end's "Followed" page.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followers', distinct=True),
        follows_count=Count('owner__follows', distinct=True)
    ).order_by('-made_at')
    serializer_class = ProfileSerializer

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followers__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieves a profile. Updates a user-owned profile.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followers', distinct=True),
        follows_count=Count('owner__follows', distinct=True)
    ).order_by('-made_at')
    serializer_class = ProfileSerializer
