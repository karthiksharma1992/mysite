from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import string

from .models import *
from .forms import *

# Create your views here.
def index(request):
    context = {'title': 'Welcome Karthik!'}
    return render(request, 'finances/index.html', context)

def accounts(request):
    if request.method == 'POST':
        form = AddAccountForm(request.POST)
        if form.is_valid():
            new_account = Account(account_name=form.cleaned_data["account_name"], current_balance=form.cleaned_data["current_balance"])
            new_account.save()
            return HttpResponseRedirect(reverse("finances:accounts"))
        else:
            return render(request, 'tasks/addGoalorAccount.html', {'newAccountForm': form, 'newGoalForm': AddGoalForm(), 'title': "Add Account or Goal"})
    accounts = Account.objects.all()
    context = {'accounts': accounts, 'title': 'My Accounts!'}
    return render(request, 'finances/accounts.html', context)

def goals(request):
    if request.method == 'POST':
        form = AddGoalForm(request.POST)
        if form.is_valid():
            #linked_account = Account.objects.get(pk=int(request.POST["account"]))
            new_goal = Goal(account=form.cleaned_data["account"], goal_name=form.cleaned_data["goal_name"], goal_target=form.cleaned_data["goal_target"], current_status=form.cleaned_data["current_status"])
            new_goal.save()
            return HttpResponseRedirect(reverse("finances:goals"))
        else:
            return render(request, 'tasks/addGoalorAccount.html', {'newAccountForm': AddAccountForm(), 'newGoalForm': form, 'title': "Add Account or Goal"})
    goals = Goal.objects.all()
    context = {'goals': goals, 'title': 'My Goals!'}
    return render(request, 'finances/goals.html', context)

def transactions(request):
    if request.method == "POST":
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            """linked_account = Account.objects.get(pk=int(form.cleaned_data["account"]))
            if (request.POST["goal"]) != '':
                linked_goal = Goal.objects.get(pk=int(form.cleaned_data["goal"]))
            else:
                linked_goal = ''"""
            new_transaction = Transaction(account=form.cleaned_data["account"], goal=form.cleaned_data["goal"], transaction_reason = form.cleaned_data["transaction_reason"], payee = form.cleaned_data["payee"], transaction_amount = form.cleaned_data["transaction_amount"], is_expense = form.cleaned_data["is_expense"], transaction_date = form.cleaned_data["transaction_date"], transaction_time = form.cleaned_data["transaction_time"] )
            new_transaction.save()
            if form.cleaned_data["is_expense"]:
                form.cleaned_data["account"].current_balance -= int(form.cleaned_data["transaction_amount"])
            else:
                form.cleaned_data["account"].current_balance += int(form.cleaned_data["transaction_amount"])
            if form.cleaned_data["goal"] is not None:
                form.cleaned_data["goal"].current_status += int(form.cleaned_data["transaction_amount"])
                form.cleaned_data["goal"].save()
            form.cleaned_data["account"].save()

            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, 'tasks/index.html', {'form': form})
    transactions = Transaction.objects.all()
    context = {'transactions': transactions, 'title': 'My Transactions!'}
    return render(request, 'finances/transactions.html', context)

def add_goal_or_account(request):
    newAccountForm = AddAccountForm()
    newGoalForm = AddGoalForm()
    context = {'newAccountForm': newAccountForm, 'newGoalForm': newGoalForm, 'title': "Add Account or Goal"}
    return render(request, 'finances/addGoalorAccount.html', context)

def add_transaction(request):
    newTransactionForm = AddTransactionForm()
    context = {'newTransactionForm': newTransactionForm, 'title': 'Add Transactions!'}
    return render(request, 'finances/addTransactions.html', context)
