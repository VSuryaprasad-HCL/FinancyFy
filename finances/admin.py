# finances/admin.py
from django.contrib import admin
from .models import Transaction, Budget, Category

admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(Category)
