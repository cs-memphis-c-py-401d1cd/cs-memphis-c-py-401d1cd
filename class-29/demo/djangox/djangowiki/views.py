from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('<h1>Django Wiki</h1>')
    # return render(request, 'djangowiki/wikiindex.html')
    if request.user.is_authenticated:
        return HttpResponse('You  r signed in! Howdy!')
    else:
        return HttpResponse('U aint logged in')

        

    
