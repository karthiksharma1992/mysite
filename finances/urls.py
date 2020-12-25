from . import views
from django.urls import path

from django.views.i18n import JavaScriptCatalog

app_name = "finances"

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.accounts, name='accounts'),
    path('goals/', views.goals, name='goals'),
    path('transactions/', views.transactions, name='transactions'),
    path('accounts/add/', views.add_goal_or_account, name='add_goal_or_account'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
]
