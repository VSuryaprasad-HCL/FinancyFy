# FinancyFy
A finance manager application will allow users to: 
* Track income and expenses 
* Create budgets Generate financial reports 
* Manage categories for transactions 
* Secure user authentication)
# Structure
```
finance_manager/
│
├── finances/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── finance_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│ 
├── manage.py
└── env/  # Virtual environment (not included in the code here)
```
# Step-by-Step Breakdown:
* Models (Track transactions, budgets, and categories)
* Views (Create views for income/expense tracking, budget management, reports, and authentication)
* Forms (For handling user input such as transaction details, budgets, etc.)
* Admin (Register models to be visible in Django Admin for easy management)
* URLs (URL routing for various views)
* User Authentication (Django’s built-in authentication system)
