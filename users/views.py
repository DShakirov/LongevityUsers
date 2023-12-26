from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .permissions import IsOwnerOrIsDoctor, IsOwnerOrIsStaff

User = get_user_model()


class UpdateUserView(generics.RetrieveUpdateAPIView):
    """Request for retrieving and updating user data.
     Use PUT/PATCh method for updating and GET method for fetching data"""
    permission_classes = (IsOwnerOrIsDoctor,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUserView(generics.DestroyAPIView):
    """Request for deleting user data. Use DELETE method"""
    permission_classes = (IsOwnerOrIsStaff,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
