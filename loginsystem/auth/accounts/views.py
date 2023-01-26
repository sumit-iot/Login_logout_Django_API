

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response  
from .serializers import RegistrationSerializer
from rest_framework import permissions
from .models import Account

class CreateAccount(APIView):
   permission_classes=[permissions.AllowAny]

   def post(self,request):
       reg_serializer=RegistrationSerializer(data=request.data)
       if reg_serializer.is_valid():
           new_user=reg_serializer.save()
           if new_user:

                
               #return Response(r.json(),status=status.HTTP_201_CREATED)

                return Response(status=status.HTTP_201_CREATED)
       #return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)