from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Thing
from .forms import ThingForm

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
    return render(request, 'thing_read.html', {'the_thing': thing})

# View for a new thing
def thing_create(request):   
    form = ThingForm(request.POST or None)
    # check submission. If data submitted, save the new thing, redirect to top/home page
    if form.is_valid():
        form.save()
        return redirect('all_things')
    return render(request, 'thing_create.html', {'form':form})

# View for a update thing
def thing_update(request,pk):   
    # first I'm going to get the thing edit/update
    thing = get_object_or_404(Thing, pk=pk)
    # Pass in the thing i want to edit ALONG WITH the form to edit it
    form = ThingForm(request.POST or None, instance = thing)
    if form.is_valid():
        form.save()
        return redirect('all_things')
    return render(request, 'thing_update.html', {'form': form, 'the_thing':thing})

# View for a delete thing
def thing_delete(request,pk):   
        # get specific thing by id 
    thing = get_object_or_404(Thing, pk=pk)
    if request.method == 'POST':
        thing.delete()
        return redirect('all_things')
    return render(request, 'thing_delete.html', {'the_thing': thing})