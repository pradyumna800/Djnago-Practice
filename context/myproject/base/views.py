from django.shortcuts import render

# Create your views here.
mylove = {
    'name': 'priyasha',
    'nick_name': 'Exception',
    'entry': 'when i was joined Qspider',
    'officially_engaged': '25-dec-2025'
    }
def home(request):
    return render(request, 'home.html', mylove)


age={'age':23}
print(age['age'])