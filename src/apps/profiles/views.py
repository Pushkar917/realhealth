from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer, UpdateProfileSerializer
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

# Create your views here.

class AllProfileAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class GetProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class GetAndUpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, username):
        user_profile=Profile.objects.get(user__username=username)
        serializer = ProfileSerializer(user_profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    
    def patch(self, request, username):
        try:
            profile=Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise "Profile Not Found"
        
        data = request.data
        logger.info(data)
        serializer = UpdateProfileSerializer(instance=profile, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

