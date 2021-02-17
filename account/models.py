from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as lazy



# Create your models here.
class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, first_name, password = None):
        if not email:
            raise ValueError("User must have an email address")
        if not first_name:
            raise ValueError("User must have an first name")
        if not password:
            raise ValueError("User must have an password" )

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user



    def create_superuser(self, email, first_name, password=None):
        user = self.create_user(
            email=email,
            first_name = first_name,
            password = password,

        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name = "email", max_length = 255, unique = True)
    first_name = models.CharField(max_length = 30, unique = True)
    password = models.CharField(lazy('password'), max_length = 128 )
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)


    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def __str__(self):
        return self.first_name


    def has_perm(self, perm, obj= None):
        return True

    def has_module_perms(self, app_label):
        return True

