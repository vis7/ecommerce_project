# Ecommerce Website In Django

## Features
- User can Register, login
- User can see product and registered User can add product to cart, remove product from cart
- User can sort product by name, price. In ascending and desending order
- There are two type of users (User and Admin), Admin can Activate, Deactivate, or promote normal user to Admin

## Setup 
Clone Repository from github
```commandline
git clone <>
cd ecommerce_project
```

Create Virualenv and install dependency
```commandline
virtualenv venv
source venv/bin/activate


pip install -r requirements.txt
```

Do Migrations
```commandline
python manage.py makemigrations
python manage.py migrate
```

Create Superuser
```commandline
python manage.py createsuperuser
```



