from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):


    def create_user(self,email,name,password=None):

        if not email:
            raise ValueError("Email must not be empty")

        
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,unique=True)

    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)


    REQUIRED_FIELDS=['name']
    USERNAME_FIELD='email'

    object=UserProfileManager()


    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

    

class Task(models.Model):
    title=models.CharField(max_length=100)
    descriptions=models.TextField()
    status=models.BooleanField(default=False)
    user=models.ForeignKey(UserProfile,related_name='tasks',on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title