from django.db import models
from users.models import MyUsers
from django.core.validators import FileExtensionValidator
from django_countries.fields import CountryField


class CompanyProfile(models.Model):
    user = models.OneToOneField(MyUsers, on_delete=models.CASCADE, related_name='company_profile')
    company_logo = models.ImageField(
        upload_to="company_logo",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])],
        null=True, blank=True
    )
    establish = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    hq_state = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=100, blank=False)
    company_description = models.CharField(max_length=500, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    is_activated = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=True)
    is_mail_verified = models.BooleanField(default=True)


    def __str__(self):
        return self.company_name
