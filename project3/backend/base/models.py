from django.db import models

# Create your models here.

class Transaction(models.Model):
    phome_number = models.CharField(max_length=12, blank=True, null=True)
    mobile_network = models.CharField(max_length=12, blank=True, null=True)
    ref_code = models.CharField(max_length=200, blank=True, null=True, unique=True)
    status = models.CharField(default='unsuccessful', max_length=50, blank=True, null=True)
    message = models.TextField(blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)