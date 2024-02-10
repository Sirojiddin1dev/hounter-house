from django.urls import path
from .views import *


urlpatterns = [
    # API views
    path('api/signin/', signin_view, name='signin_api'),
    path('api/signup/', signup_view, name='signup_api'),
    path('api/logout/', logout_view, name='logout_api'),
    path('api/get_users/', GetUser.as_view(), name='get_users_api'),
    path('api/update_user/<int:pk>/', UpdateUser.as_view(), name='update_user_api'),
    path('api/delete_user/<int:pk>/', DeleteUser.as_view(), name='delete_user_api'),

    # Create user view
    path('create_user/', create_user_view, name='create_user_url'),

    # Other paths as needed
]
