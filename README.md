# restaurant-kitchen-service
**_This program will help in managing a restaurant, namely, it will allow you to create, update or delete chefs, dishes and types of dishes using a simple and intuitive interface.**_

**The application has following database structure:**
[Kitchen_Service_d1fcaa4cdb.webp](..%2F..%2FDesktop%2FKitchen_Service_d1fcaa4cdb.webp)

### Check it out!
[Kitchen service deployed to render] (https://kitchen-41x5.onrender.com)

# Installing / Getting started

Python3 must be already installed!

## A quick introduction of the minimal setup you need to get a restaurant up and running. These steps will allow you to start the server with an empty Database!

#### shell

* git clone https://github.com/markus2812/restaurant-kitchen-service.git
* cd restaurant
* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* python manage.py runserver

# Use the following command to load prepared data from fixture:

* python manage.py loaddata restaurant_data.json

# **Features**

With this application it will be easy to:
1.     Create own profile for each chef
2.     Create a menu with food types, dishes, and chefs who can prepare these dishes,
3.     Create, update or delete Dishes, Dishtypes, Cooks
4.     Authorisation system for cooks


# Data for the test user
Login: Test
Password: y,U$_D97e%gfBN+