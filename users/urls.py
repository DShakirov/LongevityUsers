from django.urls import path
from .views import UpdateUserView, DeleteUserView

app_name = "users"

urlpatterns = [
    path("user/<str:pk>/", UpdateUserView.as_view(), name="user"),
    path("delete/<str:pk>/", DeleteUserView.as_view(), name="delete"),
    ]
