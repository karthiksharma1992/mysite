from django import forms

class AddAccountForm(forms.Form):
    accountName = forms.CharField(label= "Account Name")
    initialBalance = forms.DecimalField(label= "Initial Balance")

class AddGoalForm(forms.Form):
    goalName = forms.CharField(label= "Goal Name")
    goalTarget = forms.IntegerField(label= "Goal Target", min_value=0)
    currentStatus = froms.IntegerField(label= "Current Status", min_value=0)

class AddTransactionForm(forms.Form):
    pass
