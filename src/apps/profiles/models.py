from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import TimestampedUUIDModel
from django_countries.fields import CountryField
from django.core.validators import RegexValidator



User = get_user_model()

# Create your models here.

class Gender(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Profile(TimestampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    about_me = models.TextField(verbose_name="About Me", default="say something about yourself")
    gender = models.CharField(verbose_name="Gender", choices=Gender.choices, default=Gender.MALE, max_length=20)
    city = models.CharField(verbose_name="City", default="TimbakTu", max_length=20)
    country = CountryField(verbose_name="Country", default="IN", blank=False, null=False)


    def __str__(self):
        return f"{self.user.username}'s profile"