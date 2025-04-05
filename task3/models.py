from django.db import models, connection
from django.db.models.signals import post_save
from django.dispatch import receiver

class TransactionModel(models.Model):
    data = models.CharField(max_length=100)

@receiver(post_save, sender=TransactionModel)
def check_transaction(sender, instance, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM yourappname_transactionmodel")
        count = cursor.fetchone()[0]
        print(f"Row count in signal: {count}")
