from django.shortcuts import render

# Create your views here.
article_data = [
        {
            'id':1, 
            'title':'This is about India',
            'desc':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, nemo laborum. Placeat animi magni possimus in incidunt. Nam, neque?'
        },
        {
            'id':2, 
            'title':'This is about Bangaluru',
            'desc':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, nemo laborum. Placeat animi magni possimus in incidunt. Nam, neque?'
        },
        {
            'id':3, 
            'title':'This is about Goa',
            'desc':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, nemo laborum. Placeat animi magni possimus in incidunt. Nam, neque?'
        },
        {
            'id':4, 
            'title':'This is about Pune',
            'desc':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, nemo laborum. Placeat animi magni possimus in incidunt. Nam, neque?'
        },
        {
            'id':5, 
            'title':'This is about Odisha',
            'desc':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, nemo laborum. Placeat animi magni possimus in incidunt. Nam, neque?'
        }
    ]

new_news = [
        {
            'id' :1,
            'title':'Republic Day Celebration',
            'desc':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, nemo laborum'
        },
        {
            'id' :2,
            'title':'ISRO Launch Success',
            'desc':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, nemo laborum'
        },
        {
            'id' :3,
            'title':'Education Policy Updates',
            'desc':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, nemo laborum'
        }
    ]

events_show = [
    {
        'id':1,
        'title':'Django Workshow',
        'date':'Date: 2026-02-10',
        'desc':'Hands-on Django workshop'
    },
    {
        'id':2,
        'title':'AI Conference',
        'date':'Date: 2026-03-05',
        'desc':'Conference on AI & ML'
    },
    {
        'id':3,
        'title':'Python Bootcamp',
        'date':'Date: 2026-12-20',
        'desc':'Completed Python training'
    }
]
def home(request):
    return render(request, 'home.html', {'data':article_data})

def news(request):
    return render(request, 'news.html', {'data':new_news})

def events(request):
    return render(request, 'events.html', {'data':events_show})

def about(request):
    return render(request, 'about.html')

def read(request, id):
    for i in article_data:
        if i['id'] == id:
            context = {'data':i}
    return render(request, 'read.html', context)

def n_news(request, id):
    for i in new_news:
        if i['id'] == id:
            context = {'data':i}
    return render(request, 'news_show.html', context)

# truncatewords:n - Template filter that is used to limit the no of words that we want to display rest will get invisible
# http://127.0.0.1:8000/read/1

# for i in article_data:
#     if i['id'] == 2:
#         context = {'data':1}
#         print(context)
    # print(i)

