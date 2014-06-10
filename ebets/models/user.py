from django.models import AbstractBaseUser, BaseUserManager


class EbetsUser(AbstractBaseUser):
    identifier = models.CharField(max_length=32, unique=True)
    short_name = models.CharField(max_length=255, null=True)
    full_name = models.CharField(max_length=255, null=True)
    last_logoff = models.DateField(null=True)
    profile_url = models.URLField(max_length=255, null=True)
    avatar = models.URLField(max_length=255, null=True)
    avatar_medium = models.URLField(max_length=255, null=True)
    avatar_full = models.URLField(max_length=255, null=True)
    time_created = models.DateField(null=True)

    #A list of the field names that will be prompted for when creating a user
    #via the createsuperuser management command.
    REQUIRED_FIELDS = ['short_name']

    USERNAME_FIELD = 'identifier'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.first_name

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
            is_staff=True,
            is_verified=True,
            is_superuser=True
        )

        superuser.set_password(password)
        superuser.save()
        return superuser
