from rest_framework import serializers
from base.models import *
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
  
  
    class Meta:
        model = User
        fields = [ 'email', 'username', 'is_staff', 'is_active', 'is_emailverified', 'phone', 'passcode', 'date_of_birth', 'createdAt']

    def get_isAdmin(self,obj):
        return obj.is_staff




class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['username','email','date_of_birth',"isAdmin", 'token']

    def get_token(self, obj):
        token =RefreshToken.for_user(obj)
        return str(token.access_token)
    


