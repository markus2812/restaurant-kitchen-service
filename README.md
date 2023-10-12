# restaurant-kitchen-service
**_This program will help in managing a restaurant, namely, it will allow you to create, update or delete chefs, dishes and types of dishes using a simple and intuitive interface.**_

**The application has following database structure:**
[Kitchen_Service_d1fcaa4cdb.webp](..%2F..%2FDesktop%2FKitchen_Service_d1fcaa4cdb.webp)


# Installing / Getting started
A quick introduction of the minimal setup you need to get a restaurant up and running. These steps will allow you to start the server with an empty Database!

## git clone https://github.com/markus2812/restaurant-kitchen-service.git

* cd restaurant
* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* touch .env (Instead of "touch .env" use, please, command "echo > .env" for Windows. Fill .env file in according to .env.sample)
* python manage.py migrate
* python manage.py runserver

