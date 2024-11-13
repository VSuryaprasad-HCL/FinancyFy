# finances/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('add_budget/', views.add_budget, name='add_budget'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('report/', views.financial_report, name='financial_report'),
]
