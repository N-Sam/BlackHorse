from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'greetin': 'welcome Samuel'})

def register(request):

    return render(request,'<h2>hello world</h2>')
