from django.db import models

# Create your models here.
# models is used to defining the structure of the database
# to create in db - create table table_name(coloums_name..................)
# example:- create table student(name varchar(20), age number, email varchar(20));
# but here we can not create table directly, so for that we use python classes.
# class_name = table_name
# variables in class = coloumn names

class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(max_length=100)
    phone_no = models.IntegerField(null=True)
    regd_no = models.IntegerField(null=True)
    gender = models.CharField(max_length=20, null=True)


# python code need to be converted to sql query.
# here in django we have a command to convert python code to sql query --> python manage.py makemigrations
# check ur sql query --> python manage.py sqlmigrate application_name number_for_migration(example--> python manage.py sqlmigrate base 0001)
# to exicute this sql code to create table in database--->python manage.py migrate
# when ever i want to add a coloumn to a existing table, then we need to add 'null= True' or some default value 