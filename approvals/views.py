from rest_framework import generics, permissions

from .models import Approval
from .serializers import ApprovalSerializer


class ApprovalList(generics.ListCreateAPIView):
    """
    List approvals or create an approval if logged in
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ApprovalSerializer
    queryset = Approval.objects.all()


class ApprovalDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an approval or delete it by id if staff
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ApprovalSerializer
    queryset = Approval.objects.all()
