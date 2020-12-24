from . import views
from django.urls import path

app_name = "finances"

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.accounts, name='accounts'),
    path('goals/', views.goals, name='goals'),
    path('transactions/', views.transactions, name='transactions'),
]
