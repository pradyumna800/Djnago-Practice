from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    # create operation
    # a = Product(name='iphone', price=7000)
    # a.save()

    # Product.objects.create(name='mug', price=299)
    print(request.method)#GET #GET
    print(request.GET)#<QueryDict: {}> # <QueryDict: {'name': ['cake'], 'price': ['250']}>
    print(request.POST) #<QueryDict: {'csrfmiddlewaretoken': ['xWJ4qbFy7ZkPOntS59McOceEvdhprrrVZqfEq4N59g8mnHsEW3YtlQYSL0rAJEAB'], 'name': ['bottle'], 'price': ['299']}>


    #fetch the data from the QueryDict and save it in database
    if 'name' in request.GET: # IF FROM HAS BEEN FILLED THEN ONLY EXIECUTE IT.
        a = request.GET['name']
        b = request.GET['price']
        # print(a, b)
        Product.objects.create(
            name = a,
            price = b
        )

    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['price']
        Product.objects.create(
            name = a,
            price = b
        )
    #READ OPERATION
    # 1. get() --> QueryDict
    # 2. all() --> QuerySet
    # 3. filter() --> QuerySet

    # 1. get() method
    data = Product.objects.get(id=13)
    print(data) #Product object (5)
    print(type(data)) #<class 'base.models.Product'>
    print(data.name,data.price) #cake 250

#     #all() method
#     data1 = Product.objects.all()
#     print(data1)
#     '''
#     <QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>, <Product: Product object (4)>, <Product: Product object (5)>, <Product: Product object (6)>, <Product: Product object (7)>, <Product: Product object (8)>, <Product: Product object (9)>, <Product: Product object (10)>]>
#     '''
#     for i in data1: #<Product: Product object (1)>
#         print(i.name,i.price)
    
#     '''
#     iphone 70000
#     iphone 70000
#     iphone 70000
#     Mug 299
#     cake 250
#     bottle 499
#     bottle 499
#     apple 200
#     chocolate 199
#     DBC 299
#     '''
#     #filter method
#     data2 = Product.objects.filter(price = 70000)
#     print(data2)
#     #<QuerySet [<Product: Product object (1)>, <Product: Product object (2)>, <Product: Product object (3)>]>
#     for i in data2: #<Product: Product object (1)>
#         print(i.name,i.price)
#     '''
#     iphone 70000
#     iphone 70000
#     iphone 70000
#     '''

#     #UPDATE OPERATION
#     '''
#     1. GET THE RECORD
#     2. UPDATE THE RECORD
#     3. SAVE IT
#     '''

#     # a = Product.objects.get(id=7)
#     # a.name = 'LunchBox'
#     # a.price = 699
#     # a.save()

#     # b= Product.objects.get(id=6)
#     # b.name = 'mango'
#     # b.save()

#     #DELETE OPERATION
#     '''
#     1. GET THE RECORD
#     2. DELETE THE RECORD
#     '''
#     # a= Product.objects.get(id=6)
#     # a.delete()
#     #when u try to access a record that is not present in db it will throw u an error Product matching query does not exist.

#     # a = Product.objects.filter(name='iphone')
#     # a.delete()

#     a=Product.objects.all()
#     a.delete()
#     # return render(request,'home.html',{'data':data,'data1':data1,'a':data2})

    return render(request, 'home.html')


# """
# WHENEVER I VISIT ANY WEBPAGES FOR THE FRIRST TIME IT IS GET METHOD AND IT RETURNS EMPTY QUERYDICT.

# WHEN I FILL THE FORM AND CLICK SUBMIT request.method is post and data is present in querydict

# If you try to access from empty QueryDict it will through an error MultiValueDictKeyError at/
# """