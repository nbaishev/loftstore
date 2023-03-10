from rest_framework import viewsets

from .serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
