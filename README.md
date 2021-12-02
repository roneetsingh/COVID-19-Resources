# COVID-19-Resources

## Table of contents

- [Introduction](#introduction)
- [Demo](#demo)
- [Technology](#technology)
- [Features](#features)
- [Database](#database)
- [Run](#run)

## Introduction

• Shows most common information about the corona virus.

• Has a crowd-sourced portal to get leads on resources like beds,
oxygen cylinders, ambulances etc.

## Demo

![Screenshot 2021-12-02 154534](https://user-images.githubusercontent.com/56071565/144402629-7032d2e9-2ad5-4468-a7c6-2464198b76e0.png)
![Screenshot 2021-12-02 154557](https://user-images.githubusercontent.com/56071565/144402642-1787e27c-708e-48ec-95cb-420f8757c335.png)

The application is deployed on Heroku and can be accessed through the following link:

[Covid-19 Resources on Heroku](https://covidresourcesdj.herokuapp.com/)

The website resembles a database of leads and you can add or learn about resources.

In order to access the admin panel on "/admin" you need to provide the admin email and password.

## Technology

The application is built with:

- asgiref==3.3.4
- Django==3.2.2
- Pillow==8.2.0
- pytz==2021.1
- sqlparse==0.4.1
- waitress==2.0.0
- whitenoise==5.2.0

## Features

The application displays a virtual database that contains information about hospitals and the reasources available.

Users can do the following:

- People can add volunteers and change details of the leads.

- Track covid figures across the country with statewise data.

Admins can do the following:

- Login or logout to the admin panel.
- View all the information stored in the database. They can view/add/edit/delete resources.

## Database

 - SQLite3 database is used to store details.
 - One can see the models.py fields in model file.

## Run

To run this application
- you need to install [Technology](#technology) items using pip install -r requirements.txt
- Set your SECRET_KEY
- Set your Database
- type <b>python manage.py runserver</b>
