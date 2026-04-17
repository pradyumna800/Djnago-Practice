from django.http import HttpResponse
from django.shortcuts import render

def home(request, id):
    if id == 1:
        return HttpResponse('<h1>this is details of student 1.</h1>')
    elif id == 2:
        return HttpResponse('<h1>this is details of student 2.</h1>')
    elif id == 3:
        return HttpResponse('<h1>this is details of student 3.</h1>')
    elif id == 4:
        return HttpResponse('<h1>this is details of student 4.</h1>')
    else:
        return HttpResponse('<h1>Invalid student id.</h1>')
def student(request):
    return render(request, 'student.html')

# syntax - {% url 'pattern_name' argument %}

# static tag- is used to link css
# syntax - {% static 'file_name' %}
# but 1st load the static folder in the top of the html file - {% load static %}
