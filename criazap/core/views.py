from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario, Chats, Status,bot
from core.serializers import UsuarioSerializer, UsuarioCreateSerializer, ChatsSerializer,DetailChatsSerializer, StatusSerializer, DetailStatusSerializer, botSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['id'] = self.user.id
        data['email'] = self.user.email
        data['is_superuser'] = self.user.is_superuser
        
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["create"]:
            return UsuarioCreateSerializer
        return UsuarioSerializer

class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailStatusSerializer
        return StatusSerializer

class ChatsViewSet(ModelViewSet):
    queryset = Chats.objects.all()
    serializer_class = ChatsSerializer 
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DetailChatsSerializer
        return ChatsSerializer

class botViewSet(ModelViewSet):
    queryset = bot.objects.all()
    serializer_class = botSerializer 
    permission_classes = [AllowAny]


