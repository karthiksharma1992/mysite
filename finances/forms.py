from django.forms import ModelForm, DateInput, TimeInput
from .models import *

class AddAccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['account_name', 'current_balance']
        #accountName = forms.CharField(label= "Account Name")
        #initialBalance = forms.DecimalField(label= "Initial Balance")

class AddGoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['account', 'goal_name', 'goal_target', 'current_status']
    #goalName = forms.CharField(label= "Goal Name")
    #goalTarget = forms.IntegerField(label= "Goal Target", min_value=0)
    #currentStatus = froms.IntegerField(label= "Current Status", min_value=0)

class AddTransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'goal', 'transaction_reason', 'payee', 'transaction_amount', 'is_expense', 'transaction_date', 'transaction_time']
        widgets = {
            'transaction_date': DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select date', 'type':'date'}),
            'transaction_time': TimeInput(format=('%h%m%s'),attrs={'class':'form-control', 'placeholder':'Select time', 'type':'time'})
        }
