from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response


class SuspiciousList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": ""})


