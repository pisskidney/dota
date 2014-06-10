from django.models import AbstractBaseUser, BaseUserManager


class EbetsUser(AbstractBaseUser):
    identifier = models.CharField(max_length=32, unique=True)

    #A list of the field names that will be prompted for when creating a user
    #via the createsuperuser management command. 
    REQUIRED_FIELDS = []

    def get_full_name():
        pass

    def get_short_name():
        pass


    USERNAME_FIELD = 'identifier'


class EbetsUserManager(BaseUserManager):
    def create_user():
        pass


    def create_superuser():
        pass
