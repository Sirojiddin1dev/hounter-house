from django.urls import path
from .views import HomeListView, BannerListView, TestimonialListView, AboutHomeListView, ContactDetailView, BrandListView

urlpatterns = [
    path('api/homes/', HomeListView.as_view(), name='home-list'),
    path('api/banner/', BannerListView.as_view(), name='banner-list'),
    path('api/testimonials/', TestimonialListView.as_view(), name='testimonial-list'),
    path('api/about-homes/', AboutHomeListView.as_view(), name='about-home-list'),
    path('api/contact/', ContactDetailView.as_view(), name='contact-detail'),
    path('api/brands/', BrandListView.as_view(), name='brand-list'),
]
