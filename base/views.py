from django.shortcuts import render
# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Django is Fun'},
    {'id':3, 'name':'Anyone up for Node'}, 
    {'id':4, 'name':'Benny\'s fun room ;)'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    print(pk)
    return render(request, 'base/room.html')