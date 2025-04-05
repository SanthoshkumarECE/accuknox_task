from django.db import transaction
from django.http import HttpResponse
from .models import TransactionModel

def test_transaction(request):
    with transaction.atomic():
        TransactionModel.objects.create(data="Check row")
        return HttpResponse("Row added")
