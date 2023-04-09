from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='profile.gender')
    phone_number = serializers.CharField(source='profile.phone_number')
    profile_photo = serializers.ImageField(source='profile.profile_photo')
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name', 'gender', 'phone_number', 'country', 'city']

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self,obj):
        return obj.last_name.title()

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation
    

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]