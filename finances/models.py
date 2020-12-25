from django.db import models

# Create your models here.
class Account(models.Model):
    account_name = models.CharField(max_length=100)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Account {self.account_name} has a current balance of {self.current_balance}."

class Goal(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name = "goal_budget")
    goal_name = models.CharField(max_length=100)
    goal_target = models.DecimalField(max_digits=10, decimal_places=2)
    current_status = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"The Goal of {self.goal_name} has an amount of {self.current_status} out of {self.goal_target}"

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name="account_transaction")
    goal = models.ForeignKey(Goal, on_delete=models.PROTECT, blank=True, null=True, related_name="goal_transaction")
    transaction_reason = models.CharField(max_length=100)
    payee = models.CharField(max_length=100)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_expense = models.BooleanField(default=True)
    transaction_date = models.DateField('transaction date')
    transaction_time = models.TimeField('transaction time')
    #budget_block = models.BooleanField()

    def __str__(self):
        if self.is_expense:
            return f"An amount of {self.transaction_amount} is spent on {self.transaction_reason} on {self.transaction_date}"
        else:
            return f"An amount of {self.transaction_amount} is received on {self.transaction_reason} on {self.transaction_date}"
