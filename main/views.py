from rest_framework import generics
from .models import Home, Banner, Contacts, Testimonial, Brand
from .serializers import HomeSerializer, BannerSerializer, ContactsSerializer, TestimonialSerializer, BrandSerializer


class HomeListView(generics.ListAPIView):
    queryset = Home.objects.all().order_by('-created_at')[:5]
    serializer_class = HomeSerializer


class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all().order_by('-id')[:1]
    serializer_class = BannerSerializer


class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.all().order_by('-id')[:5]
    serializer_class = TestimonialSerializer


class AboutHomeListView(generics.ListAPIView):
    queryset = Home.objects.all().order_by('-created_at')[:4]
    serializer_class = HomeSerializer


class ContactDetailView(generics.RetrieveAPIView):
    queryset = Contacts.objects.all().order_by('-id')[:1]
    serializer_class = ContactsSerializer


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all().order_by('-id')
    serializer_class = BrandSerializer
