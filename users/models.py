from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Manager(BaseUserManager):
    """managing user creation"""

    def __create_user(self, email, nickname=None, password=None):
        if not email:
            raise ValueError("The Email field must be set!")

        user = self.model(email=self.normalize_email(email), nickname=nickname)
        user.set_password(password)

        return user

    def create_user(self, email, nickname=None, password=None):
        user = self.__create_user(email, nickname=nickname, password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname=None, password=None):
        user = self.__create_user(email, nickname=nickname, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address ✉️", max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    born_year = models.PositiveIntegerField(null=True)
    job = models.CharField(null=True)

    objects = Manager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    def __str__(self) -> str:
        return self.nickname
