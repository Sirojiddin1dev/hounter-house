from rest_framework import serializers
from .models import Video, Home, Banner, Contacts, Subscribers, Testimonial, Brand, User


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video']


class HomeSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Home
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
