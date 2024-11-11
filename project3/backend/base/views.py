from base.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
# Create your views here.






import random
import string

def generate_unique_txn_code(length=16):
    characters = string.ascii_letters + string.digits
    while True:
        txn_code = ''.join(random.choice(characters) for _ in range(length))
        if Transaction.objects.filter(txn_code=txn_code).count() == 0:
            return txn_code
        
@api_view(['POST'])
def register(request):
    data= request.data
    phone_number = data.get('phone_number')
    mobile_network= data.get('mobile_network')
    message = data.get('message')

    txn = Transaction.objects.create(
        phone_number=phone_number,
        mobile_network=mobile_network,
        message=message,
        ref_code =generate_unique_txn_code()
    )

    txn.status ='successfull'
    txn.save()

    serializer = TransactionSerializer(txn)
    return Response(serializer.data)


@api_view(['GET'])
def check_txn_with_ref_code(request, ref_code):
    txn = Transaction.objects.get(ref_code=ref_code)
    serializer =TransactionSerializer(txn)
    return Response(serializer.data)


@api_view(['PUT'])
def update_txn_message(request,pk):
    txn = Transaction.objects.get(pk=pk)
    data = request.data
    message = data.get('message')
    txn.message = message
    txn.save()

    serializer = TransactionSerializer(txn, many=False)
    return Response(serializer.data)