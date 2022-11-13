from django.shortcuts import render, redirect
from django.http import HttpResponse

from newapp.templates.aboutform import MessageForm

from .models import My_business, My_updates, Updates

# Create your views here.


def home(request):

    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():

            message = form.save(commit=False)
            message.save()
            return redirect('home')

    else:
        form = MessageForm()

    context = {'form': form}

    return render(request, 'home.html', context)


def customers(request):
    # fetch all the data from the database
    business = My_business.objects.all()

    # render the templates
    return render(request, "customers.html", {"business": business})


def about(request):
    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():

            message = form.save(commit=False)
            message.save()
            return redirect('about')

    else:
        form = MessageForm()

    context = {'form': form}
    return render(request, 'about.html', context)


def updates(request):
    update = Updates.objects.all()
    return render(request, "updates.html", {"update": update})
