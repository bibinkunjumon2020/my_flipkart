from django.db import models
from users.models import MyUsers
from django.core.validators import FileExtensionValidator
class Products(models.Model):
    """
    Product basic features model.
    """
    category_choice = (
        ('electronics', 'electronics'),
        ('fashion', 'fashion'),
        ('grocery', 'grocery'),
        ('beauty', 'beauty'),
        ('appliance', 'appliance'),
    )
    availability_choice = (
        (1, 'instore'),
        (0, 'out_of_stock'),
    )

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    product_pic = models.ImageField(
        upload_to="product_image",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])],
        null=True, blank=True
    )

    color = models.CharField(max_length=30)
    category = models.CharField(max_length=120,choices=category_choice,default='beauty')
    price = models.PositiveIntegerField()
    availability = models.BooleanField(choices=availability_choice)
    seller = models.ForeignKey(MyUsers,on_delete=models.CASCADE)  # fk for pointing to the specific user

    def __str__(self):
        return self.name


class Cart(models.Model):
    """
    Cart where a specific user adds a specific product .
    """
    choice = (
        ("incart", "incart"),
        ("order-placed", "order-placed"),
        ("cancelled", "cancelled")
    )
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE) # fk for specific product
    count = models.IntegerField(default=0)
    status = models.CharField(max_length=120,choices=choice, default='incart')
    #date = models.DateField(auto_now_add=True)
    buyer = models.ForeignKey(MyUsers,on_delete=models.CASCADE)  # fk for pointing to the specific user

    def __str__(self):
        return self.product_id+self.buyer
