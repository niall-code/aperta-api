from rest_framework import generics, permissions
from aperta_api.permissions import IsOwnerOrReadOnly

from .models import Report
from .serializers import ReportSerializer


class SuspiciousList(generics.ListCreateAPIView):
    """
    List reports or create a report if logged in.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()


class SuspiciousDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a report or delete it by id if staff.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
