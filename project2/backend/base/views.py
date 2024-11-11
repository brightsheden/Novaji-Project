from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from base.utils import sendAccountCreationEmail
from django.db import transaction
# Create your views here.




import re
from django.contrib.auth.password_validation import validate_password

@api_view(['POST'])
@transaction.atomic()
def register(request):
    data = request.data
    
    if not data:
        return Response({"message": "email and username is compulsory"}, status=status.HTTP_400_BAD_REQUEST)
    
    email = data.get('email')
    name = data.get('name').capitalize()  # Capitalize the username
    date_of_birth = data.get('date_of_birth')
    phone = data.get('phone')
    password = data.get('password')

    # Check for duplicate email
    if User.objects.filter(email=email).exists():
        return Response({"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # Check for duplicate username
    if User.objects.filter(username=name).exists():
        return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # Validate date of birth
    try:
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
    except ValueError:
        return Response({"message": "Invalid date of birth format"}, status=status.HTTP_400_BAD_REQUEST)

    # Calculate age
    today = timezone.now().date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    # Ensure user is at least 18 years old
    if age < 18:
        return Response({"message": "You must be at least 18 years old to register"}, status=status.HTTP_400_BAD_REQUEST)

    if phone:
        if len(phone) != 11:
            return Response({"message": "Phone number must be exactly 11 digits"}, status=status.HTTP_400_BAD_REQUEST)

    # Password validation
    try:
        validate_password(password)
    except ValidationError as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    # Create user
    user = User.objects.create(
        email=email,
        username=name,
        date_of_birth=date_of_birth,
        phone=phone,
        password=make_password(password)
    )

    serializer = UserSerializerWithToken(user)
    sendAccountCreationEmail(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def verify_user_email(request):
    user = request.user
    user.is_emailverified = True
    user.save()

    return Response({"message":"Email verifiied successfully"}, status=200)
