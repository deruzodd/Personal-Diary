from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserThemes(models.IntegerChoices):
    # fe7b82 = 1, 'Salmon'#, 'Pink (Salmon)'
    # e6b8e9 = 2, 'Wisteria'#, 'Violet (Wisteria)'
    # bcdca0 = 3, 'Madang'#, 'Green (Madang)'
    # f04020 = 4, 'Cinnabar'#, 'Red (Cinnabar)'
    # e0e040 = 5, 'Starship'#, 'Yellow (Starship)'
    # a0dcc0 = 6, 'Vista'#, 'Blue (Vista Blue)'
    # __empty__ = 'No theme selected'
    light = 1, 'Light'
    dark = 2, 'Dark'

class FontSizes(models.IntegerChoices):
    small = 1, 'Small'
    medium = 2, 'Medium'
    large = 3, 'Large'

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20, unique=True,
        blank=False, null=False,
    )
    theme = models.IntegerField(
        choices=UserThemes.choices, default=1,
        blank=False, null=False,
    )
    font_size = models.IntegerField(
        choices=FontSizes.choices, default=2,
        blank=False, null=False,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    # is_demo = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def __str__(self):
        return self.username
