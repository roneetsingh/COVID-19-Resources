# COVID-19-Resources

## Table of contents

- [Introduction](#introduction)
- [Demo](#demo)
- [Technology](#technology)
- [Features](#features)
- [Database Models](#database)
- [Run](#run)

## Introduction

• A crowd-sourced portal to get leads on resources like beds, oxygen 
cylinders, ambulances etc.

• People can add volunteers and change 
details of the leads.

## Demo

![Screenshot 2021-07-02 170726](https://user-images.githubusercontent.com/56071565/124269307-597e8180-db58-11eb-8126-8a8c64d31765.png)
![Screenshot 2021-07-02 170821](https://user-images.githubusercontent.com/56071565/124269323-5d120880-db58-11eb-989e-72c129cd00fc.png)
![Screenshot 2021-07-02 170856](https://user-images.githubusercontent.com/56071565/124269332-600cf900-db58-11eb-8de7-0e32b181feb4.png)

The application is deployed on Heroku and can be accessed through the following link:

[COVID-19 Resources on Heroku](https://covidresourcesdj.herokuapp.com/)

## Technology

• Tech Used: Python, Django, HTML/CSS, Bootstrap, JS.

• Utilities Used: Whitenoise, Auth Forms, Waitress.


## Features

- The application displays a table that contains list of hospitals with resources.
- A user can click on a hospital to search for the hospitals in their state and cities. Or they can search for a resource specifically too.

Users can do the following:

- Look for their cities.
- Edit the details of resources if they are volunteers.

Admins can do the following:

- Login or logout to the admin panel.
- View all the information stored in the database. They can view/add/edit/delete resources and volunteers.

Volunteers can do the following:

- Login or logout to the admin panel as a volunteer.
- View all the information stored in the database. They can view/add/edit/delete resources and add volunteers.


## Database

 - MySQL database is used to store resource(s) and their details.

## Run

To run this application
- Set your SECRET_KEY.
- Set your Database.
- type <b>python manage.py runserver</b>.
