from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class Country(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='States')
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='Cities')
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name='Cities')
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('id',)
    def __str__(self):
        return self.name

GENDER_CHOICES=(
    ('male','Male'),
    ('female','Female'),
    ('others','Others'),
)


class MyAccountManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not username:
            raise ValueError('User must has a username')
        if not email:
            raise ValueError('User must has an email')

        user = self.model(
            email = self.normalize_email(email),
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user

class Account(AbstractBaseUser):
    username = models.CharField(verbose_name='Username',max_length=200,unique=True)
    email = models.EmailField(verbose_name='Email',max_length=100,unique=True)
    firstname = models.CharField(verbose_name='First Name',max_length=100)
    lastname = models.CharField(verbose_name='Last Name',max_length=100)
    gender = models.CharField(verbose_name='Gender',max_length=10,choices=GENDER_CHOICES)
    contact = models.CharField(verbose_name='Contact No',max_length=20)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='Countries',null=True,blank=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE,related_name='States',null=True,blank=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE,related_name='Cities',null=True,blank=True)
    region = models.CharField(verbose_name='Region',max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(verbose_name="Is Admin",default=False)
    is_active = models.BooleanField(verbose_name="Is Active",default=True)
    is_staff = models.BooleanField(verbose_name="Is Staff User",default=False)
    is_superuser = models.BooleanField(verbose_name="Is Super User",default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def has_perm(self, perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
