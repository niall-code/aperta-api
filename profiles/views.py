from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    '''
    Lists existing user profiles in JSON format.
    '''
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    '''
    Handles user GET and PUT requests to fetch and return an individual
    profile view or update the profile's details in the database.
    '''
    serializer_class = ProfileSerializer

    def get_object(self, pk):
        '''
        Fetches an individual profile from the database.
        If profile does not exist, raises a 404 error.
        '''
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''
        Handles a user's GET request to view a specific profile.
        Uses `get_object` to retrieve profile, then returns data
        in JSON format.
        '''
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        '''
        Handles a user's PUT request to update their profile.
        Validates data received from user, and updates profile
        if validated. Otherwise, returns 400 error status.
        '''
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
