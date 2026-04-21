from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    '''
    1. create a model
    2. apply makemigrations & migrate
    3. open shell'
    4. perform the CRUD operation
        C- CREATE
        R- READ
        U- UPDATE
        D- DELETE

        HOW TO OPEN THE SHELL ?
        python manage.py shell ---> is the command to open the shell in the terminal

        after opening the shell we have to first import the model
        from base.models import product







        2nd method
        product.objects.create(name='cake', price=50)
        <product: product object (3)>


        # Read Operations: 3 methods
        1. get method:
        Used to fetch single records
        it is recomended to pass primery key
        returns me query dict

        example-
        a = product.objects.get(id=2)
        >>> a
        <product: product object (2)>
        >>> a.name
        'bottle'
        >>> a.price
        499

        2. all method:
        It is used to fetch all the records present in the database
        returns a query set
        a = product.objects.all()
        >>> a
        <QuerySet [<product: product object (1)>, <product: product object (2)>, <product: product object (3)>, <product: product object (4)>]>
        >>> a[0]
        <product: product object (1)>
        >>> for i in a:
        ...     print(i.name, i.price)
        ... 
        Mug 250
        bottle 499
        cake 50
        dress 500

        3. filter method:
        it is used to fetch records based on the condition & it can return single or many records.
        it returns me query set

        >>> a = product.objects.filter(price=499)
        >>> a
        <QuerySet [<product: product object (2)>]>
        >>> a[0].name
        'bottle'
        >>> a[0].price
        499
        >>> for i in a:
        ...     print(i.name, i.price, i.id)
        ... 
        bottle 499 2


        # Update Operations:
        step 1: fetch the record from the database by the help of get method 
        step 2: update the record
        step 3: save the updated record with the help of save().

        a = product.objects.get(id=3)
        >>> a
        <product: product object (3)>
        >>> a.name = 'chocolate'
        >>> a.price = 80
        >>> a.save()

        # Delete Operations:
        step 1: fetch the the record from the database using get, filter or all method
        step 2: delete the record with the help of delete(). 

        a = product.objects.filter(price=499)
        >>> a
        <QuerySet [<product: product object (2)>]>
        >>> a.delete()
        (1, {'base.product': 1})
        >>> a = product.objects.get(id=1)
        >>> a
        <product: product object (1)>
        >>> a.delete()
        (1, {'base.product': 1})
        >>> a = product.objects.all()
        >>> a 
        <QuerySet [<product: product object (3)>, <product: product object (4)>]>
        >>> a.delete()
        (2, {'base.product': 2})
    '''

    '''
    objectes= is the manager who knows how to talk with the database.
            create db queries, returns the queryset or querydict, present inside the model class.

    '''

# create a model then perform CRUD operation with the help of admit panel and shell