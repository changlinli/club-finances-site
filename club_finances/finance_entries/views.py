# Create your views here.
from django.views import generic
from django.contrib.auth import logout
from django.shortcuts import render
from finance_entries.models import FinanceTransaction
from django.db.models import Sum, Avg
import finance_entries.management.commands.readcsv2database as readcsv2db

def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html', {})

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_transactions_list'
    queryset = FinanceTransaction.objects.order_by('-transaction_time')
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['total_transaction_aggregates'] = \
            FinanceTransaction.objects.all().\
            aggregate(money_sum = Sum('amount'),
                      average = Avg('amount'))
        context['upload_csv_form'] = UploadCSVForm()
        return context

class DetailView(generic.DetailView):
    model = FinanceTransaction
    context_object_name = 'transaction'
    template_name = 'transaction_detail.html'

class ListAllView(generic.ListView):
    template_name = 'all_transactions.html'
    context_object_name = 'transactions_list'
    queryset = FinanceTransaction.objects.order_by('-transaction_time')

def upload_file(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            readcsv2db.csv2db(request.FILES['upload_file'])
            return render(request, 'upload_successful.html', {})
        else:
            return render(request, 'upload_failure.html', {'form': form})
            

from django import forms
class UploadCSVForm(forms.Form):
    upload_file = forms.FileField()
