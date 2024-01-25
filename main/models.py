from django.db import models


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
    video = models.ManyToManyField(Video)
    bathrooms = models.IntegerField()
    bedrooms = models.IntegerField()  # Fix typo in the field name
    carports = models.IntegerField()
    floors = models.IntegerField()
    descriptions = models.CharField(max_length=255)
    created_at = models.DateField()

    def __str__(self):
        return self.name


class Banner(models.Model):
    banner = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    img = models.ImageField(upload_to='banner_img/')


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

