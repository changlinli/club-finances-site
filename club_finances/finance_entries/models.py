from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FinanceTransaction(models.Model):
    heading = models.CharField(max_length = 200)
    comments = models.TextField(blank = True)
    transaction_time = models.DateField()
    cleared_by_bank_time = models.DateField(blank = True)
    authorizers = models.ManyToManyField(User)
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)

    def __str__(self):
        return self.heading
