from django.shortcuts import render, redirect
from .models import TaskModel, CompleteModel, TrashModel
# Create your views here.
def home(request):
    data = TaskModel.objects.all() #it will return a query set
    return render(request, 'home.html', {'data':data})

def add(request):
    print(request.method) #GET  #POST
    print(request.POST)
    #<QueryDict: {'csrfmiddlewaretoken': ['NVBzE3VsIoMXHqbe28mDSt7rRIjLvvD9fp79EW3ZKFAugKa0T2yUp7RF7vtWNIMP'], 'title': ['Django'], 'desc': ['Need to work on model']}>
    if request.method == 'POST' and request.POST['title'] and request.POST['desc']:
        a = request.POST['title']
        b = request.POST['desc']
        TaskModel.objects.create(
            title=a,
            desc=b
        )
        return redirect('home') #it will redirect to the mentionted page after submiting the form [for that we need to inport redirect() from django.shortcuts module]
    elif request.method == 'POST':
        return render(request, 'add.html',{'notic':'data should me mentionted before submit'})
    return render(request, 'add.html')

def complete(request): # used to render complete page with the data present in the complete page
    data = CompleteModel.objects.all()
    return render(request, 'complete.html',{'data':data})

def trash(request):
    data = TrashModel.objects.all()
    return render(request, 'trash.html', {'data':data})

def about(request):
    return render(request, 'about.html')

# home page update method
def update(request, id):
    a = TaskModel.objects.get(id=id)
    print(a, a.title, a.desc)

    if request.method == 'POST':
        b = request.POST['title']
        c = request.POST['desc']
        print(b, c)
        a.title = b
        a.desc = c
        a.save()
        return redirect('home')
    return render(request, 'update.html', {'data':a})


# home page complete button
'''
when i click on complete button of any record the id should be passed in the url.
we need to create a complete model and store that porticular record in it.
after storing it in CompleteModel we need to delete from the TaskModel.
'''
def complete_(request, id):
    a = TaskModel.objects.get(id=id)
    # print(a)
    CompleteModel.objects.create(
        title = a.title,
        desc = a.desc
    )
    a.delete()
    return redirect('complete')

# home page delete button
def delete_(request, id):
    a = TaskModel.objects.get(id=id)
    TrashModel.objects.create(
        title = a.title,
        desc = a.desc
    )
    a.delete()
    return redirect('trash')


#home page complete_all button
def complete_all(request):
    a = TaskModel.objects.all()
    print(a) #<QuerySet [<TaskModel: TaskModel object (5)>, <TaskModel: TaskModel object (6)>]>
    for i in a:
        CompleteModel.objects.create(
            title = i.title,
            desc = i.desc
        )
    a.delete()
    return redirect('complete')

#home page delete_all button
def delete_all(request):
    a = TaskModel.objects.all()
    for i in a:
        TrashModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('trash')

#complete page 
#delete button - get the record from completemodel then create the record in the trashmodel then delete it from the completemodel
def c_delete(request, id):
    a = CompleteModel.objects.get(id = id)
    TrashModel.objects.create(
        title = a.title,
        desc = a.desc
    )
    a.delete()
    return redirect('trash')
#delete all button - get all the records from the completemodel then create the records one after the other in trashmodel then delete it in completemodel.
def c_delete_all(request):
    a = CompleteModel.objects.all()
    for i in a:
        TrashModel.objects.create(
            title = i.title,
            desc = i.desc
        )
    a.delete()
    return redirect('trash')

#complete page
# restore button - get the recored from the completemodel
def c_restore(request, id):
    a = CompleteModel.objects.get(id=id)
    print(a)
    TaskModel.objects.create(
        title = a.title,
        desc = a.desc
    )
    a.delete()
    return redirect('home')
def c_restore_all(request):
    a = CompleteModel.objects.all()
    for i in a:
        TaskModel.objects.create(
            title = i.title,
            desc = i.desc
        )
    a.delete()
    return redirect('home')
#trash page
#delete button - get the record from the trashmodel then delete it parmanetly with the help of delete method
def t_delete(request, id):
    a = TrashModel.objects.get(id = id)
    a.delete()
    return redirect('trash')
# delete all button - get all the records fro the trashmodel then delete it.
def t_delete_all(request):
    a = TrashModel.objects.all()
    a.delete()
    return redirect('trash')