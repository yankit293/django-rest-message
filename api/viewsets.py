
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import userSerializers, messageSerializers, RegisterSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .models import messages
from rest_framework.permissions import AllowAny
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
 
 
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = userSerializers(user)
    return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class messagesviewsets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = messages.objects.all()
    serializer_class = messageSerializers
    throttle_classes = [UserRateThrottle]
    
    def perform_create(self, serializer):
        kwargs = {
        'created_by':{
            'id': self.request.user.id,
            'username': self.request.user.username,
            'email': self.request.user.email
        } 
        }
        serializer.save(**kwargs)
