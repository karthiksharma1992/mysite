from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    context = {}
    return render(request, 'finances/index.html', context)

def accounts(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'finances/accounts.html', context)

def goals(request):
    goals = Goal.objects.all()
    context = {'goals': goals}
    return render(request, 'finances/goals.html', context)

def transactions(request):
    transactions = Transaction.objects.all()
    context = {'transactions': transactions}
    return render(request, 'finances/transactions.html', context)
