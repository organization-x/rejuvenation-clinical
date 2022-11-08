from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomAccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, country, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must have a password.")
        if not first_name:
            raise ValueError("Users must have a first name.")
        if not last_name:
            raise ValueError("Users must have a last name.")
        if not country:
            raise ValueError("Users must have a country.")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, country, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            country=country,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    # LATER: CREATE A 'LAB' USER

class Account(AbstractBaseUser):

    email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
    first_name              = models.CharField(max_length=30)
    last_name               = models.CharField(max_length=30)
    country                 = models.CharField(max_length=50)
    # create a new user
    # create a superuser
    # creates a custom user to get the sms 2fa ready:
    phone_number            = models.CharField(max_length = 12)
    date_joined             = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'country']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_user(self):
        return self.USERNAME_FIELD
