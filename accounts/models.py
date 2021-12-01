from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import activate

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, full_name, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not full_name:
            raise ValueError('Users must have a full name')
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        

        user_obj = self.model(
             full_name = full_name,
            email = self.normalize_email(email)
           
        )

        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, full_name, email, password=None):
        user = self.create_user( 
            full_name,
            email,
            password=password,
            is_staff=True
        )

        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            full_name,
            email, 
            password=password,
            is_staff=True,
            is_admin=True
        )

        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

