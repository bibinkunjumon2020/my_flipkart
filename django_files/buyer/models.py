from django.db import models
from users.models import MyUsers
class BuyerModel(models.Model):

    sex_choices = (
        ("Male", "male"),
        ('Female', 'female'),
        ('Not Say', 'Not Say'),
    )
    # buyer
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    sex = models.CharField(choices=sex_choices, max_length=50, null=True, blank=True)
    buyer = models.ForeignKey(MyUsers,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.first_name
