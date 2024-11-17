from rest_framework import generics, permissions

from reports.models import Report
from posts.models import Post
from reports.serializers import ReportSerializer


class SuspiciousList(generics.ListCreateAPIView):
    """
    List reports or create a report if logged in.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        reported_post = Post.objects.get(id=post_id)
        serializer.save(
            owner=self.request.user,
            reported_post=reported_post
        )


class SuspiciousDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a report or delete it by id if staff.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
