from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, name, email, username, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('name', max_length=64)
    email = models.EmailField('email address', max_length=255, unique=True, db_index=True,)
    username = models.CharField('username', max_length=255, unique=True, null=True)

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as active.  Unselect instead of deleting.')

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'username']

    class Meta:
        db_table = 'auth_user'
        # abstract = True
        ordering = ['username', 'name', 'email']
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True,
                                related_name='profile')

    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)

    location = models.CharField("Location", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)

    def __str__(self):
        return "%s's profile".format(self.user)
