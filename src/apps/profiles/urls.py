from django.urls import path
from .views import GetProfileAPIView, GetAndUpdateProfileAPIView, AllProfileAPI


urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path("update/<str:username>/", GetAndUpdateProfileAPIView.as_view(), name="update_profile"),
    path("getAllProfiles", AllProfileAPI.as_view(), name="get-all-profile"),
    path("getProfileOf/<str:username>/", GetAndUpdateProfileAPIView.as_view(), name="get-a-profile"),
]