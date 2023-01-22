from django.db import models
from users.models import MyUsers

# seller
class SellerModel(models.Model):
    seller_name = models.CharField(max_length=150, blank=True, null=True)
    seller_reg = models.CharField(max_length=500, blank=True, null=True)
    founded = models.DateField(blank=True, null=True)
    seller = models.ForeignKey(MyUsers,on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.seller_name
