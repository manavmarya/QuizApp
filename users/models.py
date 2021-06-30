from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import Group
from myquiz.settings import AUTH_USER_MODEL


class UserManager(BaseUserManager):
    def create_user(self, email, is_staff, is_superuser, password, name, teachers=None, class_name=12):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            teachers = teachers,
            class_name = class_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, is_staff, is_superuser, password, name, teachers, class_name):
        user = self.create_user(
            email,
            password=password,
            name=name,
            teachers=teachers,
            is_staff=is_staff,
            class_name=class_name
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, True, True, password, **kwargs)
        user.save(using=self._db)
        return user

minmax_error = "Class not valid"

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Email Address", max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    class_name = models.IntegerField(null=True, validators=[MaxValueValidator(13, minmax_error), MinValueValidator(0, minmax_error)])
    teachers = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, null=True)
    objects = UserManager()
    def __str__(self):
        return "{0} of Class {1}".format(self.name,self.class_name)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_absolute_url(self):
        return "/users/{0}/".format(self.pk)

    def add_group(self):
        if (self.is_staff):
            group_name = 'Teachers'
            self.teachers=None
        else:
            group_name = 'Students'
        my_group = Group.objects.get(name=group_name)
        my_group.user_set.add(self)

    def get_quizes(self):
        return self.quiz_set.all()