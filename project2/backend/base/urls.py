from django.urls import path
from base.views import *
urlpatterns = [
   # path('login/',MyTokenObtainPairView.as_view(),
   #      name='token_obtain_pair'),

    path('register', register),
    path('verify_email', verify_user_email)

   
]
