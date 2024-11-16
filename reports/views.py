from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Report
from .serializers import ReportSerializer


class SuspiciousList(generics.ListCreateAPIView):
    """
    List reports or create a report if logged in.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()


class SuspiciousDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a report or delete it by id if staff.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
