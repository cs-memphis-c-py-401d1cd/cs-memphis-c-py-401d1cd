from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Thing

def index(request):
    # return HttpResponse("<h1>HOWDY, world. Looks like it worked.</h1>")
    return render(request, 'base.html')

# This view renders all things
def all_things(request):
    object_things = Thing.objects.all()
    return render(request, 'thing_list.html', {'all_object_things': object_things})

# This view will display a specific thing
def thing_detail(request, pk):
    # get specific thing by id 
    thing = get_object_or_404(Thing, pk=pk)
    return render(request, 'thing_detail.html', {'the_thing': thing})




