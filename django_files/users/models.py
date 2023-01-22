from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import FileExtensionValidator


class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.is_admin = False
        user.is_active = False
        user.is_staff = False
        user.is_superadmin = False
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save()
        return user


class MyUsers(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    role = models.CharField(max_length=120,null=True,blank=True)
    # address both buyer and seller
    profile_logo = models.ImageField(
        upload_to="buyer_image",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"])],null=True,blank=True)

    building_name = models.CharField(max_length=500,null=True,blank=True)
    lane1 = models.CharField(max_length=500,null=True,blank=True )
    lane2 = models.CharField(max_length=500,null=True,blank=True )
    state = models.CharField(max_length=200,null=True,blank=True )
    district = models.CharField(max_length=200,null=True,blank=True )
    country = models.CharField(max_length=200,null=True,blank=True)
    place = models.CharField(max_length=200,null=True,blank=True )
    pin = models.PositiveIntegerField(null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)

    # auto add fields

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    # admin user stuff

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # # seller
    #
    # seller_name = models.CharField(max_length=150, blank=True, null=True)
    # seller_reg = models.CharField(max_length=500, blank=True, null=True)
    # founded = models.DateField(blank=True, null=True)

    # # buyer
    #
    # dob = models.DateField(null=True, blank=True)
    # first_name = models.CharField(max_length=50,null=True,blank=True)
    # last_name = models.CharField(max_length=50,null=True,blank=True)
    # sex = models.CharField(choices=sex_choices, max_length=50,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'
    #
    def __str__(self):
        return self.email

    # def get_role(self):
    #     user_role = None
    #     if self.role == 1:
    #         user_role = 'seller'
    #     elif self.role == 2:
    #         user_role = 'buyer'
    #     return user_role

    # def get_full_name(self):
    #     """
    #     Return the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = "%s %s" % (self.first_name, self.last_name)
    #     return full_name
