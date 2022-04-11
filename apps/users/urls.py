from django.urls import path
from .views import *

urlpatterns = [
    path('me',CreateUserView.as_view()),
    path('user/all', ListUserView.as_view()),
    path('update/<str:username>',UpdateUserView.as_view()),
    path('<str:username>/delete', DeleteUserView.as_view()),
]