from rest_framework import serializers
from base.models import *

class TransactionSerializer(serializers.ModelSerializer):
        class Meta:
                models = Transaction
                fields ="__all__"