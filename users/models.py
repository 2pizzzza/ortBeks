from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

from . import validators as val


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields['role'] = 'Администратор'
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    ROLES = (
        ('Учитель', 'Учитель'),
        ('Студент', 'Студент')
    )

    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    patronymic = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, choices=ROLES, default=ROLES[1][1], null=True)

    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.role} {self.firstname} {self.lastname}'

    def save(self, *args, **kwargs):
        if self.password and not str(self.password).startswith(('pbkdf2_sha256$', 'bcrypt')):
            self.set_password(self.password)
        super().save(*args, **kwargs)


class Profile(models.Model):
    LANGUAGES = (
        ('Кыргызский', 'Кыргызский'),
        ('Русский', 'Русский'),
        ('Английский', 'Английский'),
    )

    SEX = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    language = models.CharField(max_length=50, choices=LANGUAGES)
    _class = models.CharField(max_length=4, validators=[val.validate_class])
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=50, choices=SEX)
    phone = models.CharField(max_length=20, validators=[val.validate_phone])
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль студента {self.user.lastname} {self.user.firstname}'
