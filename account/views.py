from django.shortcuts import render, redirect
from main.models import User
from main.serializers import UserSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView


@api_view(['POST'])
def signin_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                status = 200
                data = {
                    'status': status,
                    'username': username,
                }
            else:
                status = 403
                message = "Invalid Password or Username!"
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = 'This User is not defined! '
            data = {
                'status': status,
                'message': message,
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def signup_view(request):
    username = request.POST.get("username")
    password = request.POST.get('password')
    phone_number = request.POST.get('phone_number')
    new = User.objects.create_user(
        username=username,
        password=password,
        phone_number=phone_number
    )
    ser = UserSerializers(new)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'data':'sucses'})


class GetUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UpdateUser(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class DeleteUser(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


def create_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        User.objects.create_user(username=username, password=password, phone_number=phone_number)
        return redirect('index_url')
    return render(request, 'index.html')



