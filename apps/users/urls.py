from django.urls import path
from .views import *

urlpatterns = [
    path('create',CreateUserView.as_view()),
    path('create/list', ListUserView.as_view()),
    path('<int:pk>',UpdateUserView.as_view()),
    path('<int:pk>/delete', DeleteUserView.as_view()),
]