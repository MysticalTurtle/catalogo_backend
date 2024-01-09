from rest_framework import viewsets, permissions, generics,status
from ecomerce.models import *
from ecomerce.serializers import *
# from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes,action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.AllowAny]
        elif(self.action in ['retrieve']):
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny 
    ]
    serializer_class = UserSerializer  


class TheAutentication(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)


class LoginCustom(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        user_data = UserSerializer(user, context={'request': request}).data
        response.data['user'] = user_data
        return response