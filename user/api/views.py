from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from .serializers import UserSerialzer


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
