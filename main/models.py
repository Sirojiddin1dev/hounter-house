from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    img = models.ImageField(upload_to='user_image/')
    phone_number = models.CharField(max_length=13, verbose_name='Telefon raqam', null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Video(models.Model):
    video = models.FileField(upload_to='home_video/')


class Home(models.Model):
    name = models.CharField(max_length=255)
    home_img = models.ImageField(upload_to='home_img/')
    price = models.IntegerField()
    user_img = models.ImageField(upload_to='user_img/')
    user_name = models.CharField(max_length=255)
    user_location = models.CharField(max_length=255)
    Status = (
        ('popular', 'popular'),
        ('new house', 'new house'),
        ('best deals', 'best deals')
    )
    status = models.CharField(max_length=50, choices=Status)
    Category = (
        ('House', 'House'),
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment')
    )
    category = models.CharField(max_length=50, choices=Category)
    # video = models.ManyToManyField(Video)
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()  # Fix typo in the field name
    carports = models.IntegerField()
    floors = models.IntegerField()
    descriptions = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Contacts(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255, null=True)
    Subject = models.CharField(max_length=255, null=True)
    Message = models.TextField(null=True)


class Subscribers(models.Model):
    Email = models.CharField(max_length=255)


class Testimonial(models.Model):
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Content = models.TextField(null=True)
    img = models.ImageField(upload_to='article_img/')
    author_img = models.ImageField(upload_to='author_img/')
    rating = models.DecimalField(max_digits=8, decimal_places=2)
    PublishDate = models.DateField(null=True)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='brand_img/')


class Banner(models.Model):
    banner = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    img = models.ImageField(upload_to='banner_img/')