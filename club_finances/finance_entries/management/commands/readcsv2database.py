from django.core.management.base import BaseCommand, CommandError
from finance_entries.models import FinanceTransaction
import csv
import datetime

strptime = datetime.datetime.strptime
strftime = datetime.datetime.strftime

def csv2db(csv_file):
    reader = csv.DictReader(csv_file)
    list_of_dictionaries = [row for row in reader]
    for dictionary in list_of_dictionaries:
        dictionary['transaction_time'] = \
            strptime(dictionary['transaction_time'], '%m/%d/%y').\
            strftime('%Y-%m-%d')

        dictionary['cleared_by_bank_time'] = '2013-01-01'
        transaction = FinanceTransaction(**dictionary)
        transaction.save()

class Command(BaseCommand):
    """ Takes a CSV file and saves it into the database driving a model. """
    args = '<name_of_csv_file> <name_of_model> ...'
    help = __doc__

    def handle(self, *args, **options):
        csv_file = open(args[0])
        csv2db(csv_file)
