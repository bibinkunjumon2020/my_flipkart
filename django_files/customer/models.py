from django.db import models
#from ..users.models import MyUsers
from users.models import MyUsers
from django.core.validators import FileExtensionValidator
from django_countries.fields import CountryField


class CustomerProfile(models.Model):
    user = models.OneToOneField(MyUsers, on_delete=models.CASCADE, related_name='customer_profile')
    customer_image = models.ImageField(
        upload_to="customer_image",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])],
        null=True, blank=True
    )
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.first_name
