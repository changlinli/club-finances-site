from django.contrib import admin
from finance_entries.models import FinanceTransaction

class FinanceTransactionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'transaction_time', 'cleared_by_bank_time',
                 'amount')
    ordering = ['-transaction_time']

admin.site.register(FinanceTransaction, FinanceTransactionAdmin)
