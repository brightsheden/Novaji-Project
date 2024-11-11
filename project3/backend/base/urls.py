from django.urls import path
from .views import register, check_txn_with_ref_code, update_txn_message

urlpatterns = [
    path('register/', register, name='register'),
    path('check-txn/<str:ref_code>/', check_txn_with_ref_code, name='check-txn'),
    path('update_txn/<str:pk>/', update_txn_message)
]