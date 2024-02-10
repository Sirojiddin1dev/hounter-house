from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.decorators import permission_classes
from .models import *
from .serializers import HomeSerializer, BannerSerializer, ContactsSerializer, TestimonialSerializer, BrandSerializer
from datetime import datetime, timedelta
from django.db.models import Count
from django.db.models.functions import ExtractDay, ExtractMonth, ExtractWeek
import calendar
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


@permission_classes([IsAuthenticated])
def home_page_view(request):
    home = Home.objects.filter(status='new house').order_by('-id')
    context = {
        'a': PegenatorPage(home, 5, request)
    }
    return render(request, 'home_page.html', context)


@permission_classes([IsAuthenticated])
def popular_home_view(request):
    home = Home.objects.filter(status='popular').order_by('-id')
    context = {
        'a': PegenatorPage(home, 5, request)
    }
    return render(request, 'popular_home.html', context)


@permission_classes([IsAuthenticated])
def best_home_view(request):
    home = Home.objects.filter(status='best deals').order_by('-id')
    context = {
        'a': PegenatorPage(home, 5, request)
    }
    return render(request, 'best_deals.html', context)


@permission_classes([IsAuthenticated])
def apartment_view(request):
    home = Home.objects.filter(category='Apartment').order_by('-id')
    context = {
        'a': PegenatorPage(home, 5, request)
    }
    return render(request, 'apartment.html', context)


@permission_classes([IsAuthenticated])
def house_view(request):
    home = Home.objects.filter(category='House').order_by('-id')
    context = {
        'a': PegenatorPage(home, 5, request)
    }
    return render(request, 'house.html', context)


@permission_classes([IsAuthenticated])
def villa_view(request):
    home = Home.objects.filter(category='Villa').order_by('-id')
    context = {
        'a': PegenatorPage(home, 5, request)
    }
    return render(request, 'villa.html', context)


@permission_classes([IsAuthenticated])
def banner_view(request):
    brand = Brand.objects.all()
    banner = Banner.objects.all()
    context = {
        'a': PegenatorPage(brand, 5, request),
        'ab': PegenatorPage(banner, 5, request)
    }
    return render(request, 'banner.html', context)


@permission_classes([IsAuthenticated])
def create_home_view(request):
    if request.method == 'POST':
        # Get data from POST request
        name = request.POST.get('name')
        home_img = request.FILES.get('home_img')
        price = request.POST.get('price')
        user_img = request.FILES.get('user_img')
        user_name = request.POST.get('user_name')
        user_location = request.POST.get('user_location')
        status = request.POST.get('status')
        category = request.POST.get('category')
        bathrooms = request.POST.get('bathrooms')
        bedrooms = request.POST.get('bedrooms')
        carports = request.POST.get('carports')
        floors = request.POST.get('floors')
        descriptions = request.POST.get('descriptions')
        created_at = request.POST.get('created_at')

        # Create a new Home object
        Home.objects.create(
            name=name,
            home_img=home_img,
            price=price,
            user_img=user_img,
            user_name=user_name,
            user_location=user_location,
            status=status,
            category=category,
            bathrooms=bathrooms,
            bedrooms=bedrooms,
            carports=carports,
            floors=floors,
            descriptions=descriptions,
            created_at=created_at
        )

        return HttpResponse("Home object created successfully!")

    return redirect("index_url")


@permission_classes([IsAuthenticated])
def update_home_view(request, pk):
    home = Home.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        home_img = request.FILES.get('home_img')
        price = request.POST.get('price')
        user_img = request.FILES.get('user_img')
        user_name = request.POST.get('user_name')
        user_location = request.POST.get('user_location')
        status = request.POST.get('status')
        category = request.POST.get('category')
        bathrooms = request.POST.get('bathrooms')
        bedrooms = request.POST.get('bedrooms')
        carports = request.POST.get('carports')
        floors = request.POST.get('floors')
        descriptions = request.POST.get('descriptions')
        created_at = request.POST.get('created_at')
        home.name = name
        home.home_img = home_img
        home.price = price
        home.user_img = user_img
        home.user_name = user_name
        home.user_location = user_location
        home.status = status
        home.category = category
        home.bathrooms = bathrooms
        home.bedrooms = bedrooms
        home.carports = carports
        home.floors = floors
        home.descriptions = descriptions
        home.created_at = created_at
        home.save()
        return redirect("home_page_url")
    context = {
        'home_single': home
    }
    return render(request, 'popular_home.html', context)


@permission_classes([IsAuthenticated])
def delete_home_view(request, pk):
    home = Home.objects.get(pk=pk)
    home.delete()
    return redirect('home_page_url')


@permission_classes([IsAuthenticated])
def delete_user_view(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('index_url')


# Brand views
@permission_classes([IsAuthenticated])
def create_brand(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES['img']
        Brand.objects.create(name=name, img=img)
        return HttpResponse("Home object created successfully!")

    return redirect('index_url')


@permission_classes([IsAuthenticated])
def update_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.name = request.POST['name']
        if 'img' in request.FILES:
            brand.img = request.FILES['img']
        brand.save()
        return redirect('banner_url')


@permission_classes([IsAuthenticated])
def delete_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    brand.delete()
    return redirect('banner_url')


@permission_classes([IsAuthenticated])
def create_banner(request):
    if request.method == 'POST':
        banner_text = request.POST['banner']
        description = request.POST.get('description', None)
        img = request.FILES['img']
        Banner.objects.create(banner=banner_text, description=description, img=img)
        return HttpResponse("Home object created successfully!")
    return redirect('index_url')  # Assuming you have a URL named 'banner_list'


@permission_classes([IsAuthenticated])
def update_banner(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.banner = request.POST['banner']
        banner.description = request.POST.get('description', None)
        if 'img' in request.FILES:
            banner.img = request.FILES['img']
        banner.save()
        return redirect('banner_url')


@permission_classes([IsAuthenticated])
def delete_banner(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    banner.delete()
    return redirect('banner_url')


@permission_classes([IsAuthenticated])
def home_view(request):
    all_register = Home.objects.all().order_by('id').count()
    day = datetime.today() - timedelta(days=1)
    month = datetime.today() - timedelta(days=30)
    today = Home.objects.filter(created_at__gte=day).count()
    months = Home.objects.filter(created_at__gte=month).count()
    qs = Home.objects.filter(
        created_at__gte=month
    ).annotate(
        day=ExtractDay("created_at"),
        mon=ExtractMonth('created_at'),
    ).values(
        'day', 'mon'
    ).annotate(
        n=Count('pk')
    ).order_by('mon')
    mon_list = []
    for i in qs:
        i['mon'] = (calendar.month_abbr[i['mon']])
        if len(mon_list) >= 30:
            del mon_list[0]
            mon_list.append(i)
        else:
            mon_list.append(i)
    context = {
       "all_register":all_register,
       "today":today,
       "month":months,
        "qs": mon_list,
        'user': User.objects.all().order_by('-id')[:4]
    }
    print(today)
    return render(request, 'index.html',context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
    return render(request, 'login.html')


def PegenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


@permission_classes([IsAuthenticated])
def user_view(request):
    user = User.objects.all().order_by('-id')
    context = {
        'a': PegenatorPage(user, 5, request)
    }
    return render(request, 'users.html', context)


def user_detail_view(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'user-detail.html', context)


def update_user_view(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        img = request.FILES.get('img')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        user.username=username
        user.email=email
        user.phone_number=phone_number
        user.img=img
        user.save()
        return HttpResponse("Home object created successfully!")

    return redirect('user_detail_url')