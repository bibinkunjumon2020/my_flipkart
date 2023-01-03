from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


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
    seller = 1
    buyer = 2
    role_choices = (
        (seller, 'seller'),
        (buyer, 'buyer')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    role = models.PositiveSmallIntegerField(choices=role_choices, blank=True, null=True)
    password = models.CharField(max_length=300)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','phone_number','role']

    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email+self.first_name+self.last_name+self.phone_number

    def get_role(self):
        user_role = None
        if self.role == 1:
            user_role = 'seller'
        elif self.role == 2:
            user_role = 'buyer'
        return user_role

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name
