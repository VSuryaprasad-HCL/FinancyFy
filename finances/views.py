# finances/views.py
from django.shortcuts import render, redirect
from .models import Transaction, Budget, Category
from .forms import TransactionForm, BudgetForm
from django.db.models import Sum

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'add_budget.html', {'form': form})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'budget_list.html', {'budgets': budgets})

def financial_report(request):
    total_income = Transaction.objects.filter(category__name="Income").aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(category__name="Expense").aggregate(Sum('amount'))['amount__sum'] or 0
    net_balance = total_income - total_expense
    return render(request, 'financial_report.html', {'total_income': total_income, 'total_expense': total_expense, 'net_balance': net_balance})
