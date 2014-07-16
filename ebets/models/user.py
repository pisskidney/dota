import datetime
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class EbetsAuthenticationBackend(object):
    def authenticate(self, identifier=None):
        try:
            return EbetsUser.objects.get(identifier=identifier)
        except EbetsUser.DoesNotExist:
            return None

    def get_user(self, identifier):
        try:
            return EbetsUser.objects.get(pk=identifier)
        except EbetsUser.DoesNotExist:
            return None


class EbetsUserManager(BaseUserManager):
    def create_user(self, identifier, password=False, short_name=None,
                    full_name=None, last_logoff=None, profile_url=None,
                    avatar=None, avatar_medium=None, avatar_full=None,
                    time_created=None):
        return self.model.create(
            identifier, password, short_name,
            full_name, last_logoff, profile_url,
            avatar, avatar_medium, avatar_full,
            time_created, commit=True
        )

    def create_superuser(self, identifier, short_name, password):
        superuser = self.model(
            identifier=identifier,
            short_name=short_name,
            is_admin=True,
            is_superuser=True
        )

        superuser.set_password(password)
        superuser.save()
        return superuser


class EbetsUser(AbstractBaseUser, PermissionsMixin):
    identifier = models.CharField(max_length=32, unique=True)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    last_logoff = models.DateTimeField(null=True, blank=True)
    profile_url = models.URLField(max_length=255, null=True, blank=True)
    avatar = models.URLField(max_length=255, null=True, blank=True)
    avatar_medium = models.URLField(max_length=255, null=True, blank=True)
    avatar_full = models.URLField(max_length=255, null=True, blank=True)
    time_created = models.DateTimeField(null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    #A list of the field names that will be prompted for when creating a user
    #via the createsuperuser management command.
    REQUIRED_FIELDS = ['short_name']

    USERNAME_FIELD = 'identifier'

    objects = EbetsUserManager()

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.short_name

    @classmethod
    def create(cls, identifier, password=None, short_name=None,
               full_name=None, last_logoff=None, profile_url=None,
               avatar=None, avatar_medium=None, avatar_full=None,
               time_created=None, commit=True):
        user = cls(
            identifier=identifier,
            password=password,
            short_name=short_name,
            full_name=full_name,
            last_logoff=last_logoff,
            profile_url=profile_url,
            avatar=avatar,
            avatar_medium=avatar_medium,
            avatar_full=avatar_full,
            time_created=time_created
        )

        user.set_password(password)
        if commit:
            user.save()
        return user

    def update_from_steam_data(self, info_dict):
        self.full_name = info_dict.pop('realname')
        self.short_name = info_dict.pop('personaname')
        self.avatar_medium = info_dict.pop('avatarmedium')
        self.avatar_full = info_dict.pop('avatarfull')
        self.last_logoff = datetime.datetime.fromtimestamp(
            info_dict.pop('lastlogoff')
        )
        self.time_created = datetime.datetime.fromtimestamp(
            info_dict.pop('timecreated')
        )
        self.profile_url = info_dict.pop('profileurl')
        self.save()

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        app_label = 'ebets'
