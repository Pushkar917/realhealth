
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(read_only=True)

    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name", "full_name", "email", "id", "phone_number", "about_me", "gender", "country", "city"]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name}{last_name}"
    
class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    class Meta:
        model = Profile
        fields=["phone_number",
                "about_me",
                "gender",
                "country",
                "city"]
        
    def update(self, instance, validated_data): 
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.about_me = validated_data.get('about_me', instance.about_me)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
        
