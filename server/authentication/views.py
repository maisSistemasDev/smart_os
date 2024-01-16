from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response  
from .serializers import RegistrationSerializer, UsersSerializer
from .models import  Account
import os
import requests
from django.utils import timezone
from utils.logger import log_decorator

class CreateAccount(APIView):
    permission_classes = [permissions.AllowAny]

    @log_decorator
    def post(self, request):
        reg_serializer = RegistrationSerializer(data=request.data)

        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                token_data = self.get_auth_token(new_user, request.data['password'])
                if token_data:
                    return Response(token_data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Failed to retrieve authentication token."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  
    @log_decorator
    def get_auth_token(self, user, password):
        client_id =  os.environ.get('CLIENT_ID')
        client_secret =  os.environ.get('CLIENT_SECRET')
        try:
            print(client_id)
            print(client_secret)
            print(user.email)
            response = requests.post('http://127.0.0.1:8000/api-auth/token', data={
                'username': user.email,
                'password': password,
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': 'password'
            })
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error retrieving auth token: {e}")
            return None



class CurrentUser(APIView):
   permission_classes = (permissions.IsAuthenticated,)

   @log_decorator
   def get(self, request):
       serializer = UsersSerializer(self.request.user)
       account = Account.objects.get(id=serializer.data.get('id'))
       account.last_login = timezone.now()
       account.save() 
       return Response(serializer.data)

