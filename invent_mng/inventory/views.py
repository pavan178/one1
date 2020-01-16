from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def display_item1(request):
    items = Item1.objects.all()
    context = {
        'items': items,
        'header': 'Item1'
    }
    return render(request, 'index.html', context)


def display_item2(request):
    items = Item2.objects.all()
    context = {
        'items': items,
        'header': 'Item2'
    }
    return render(request, 'index.html', context)


def display_item3(request):
    items = Item3.objects.all()
    context = {
        'items': items,
        'header': 'Item3'
    }
    return render(request, 'index.html', context)


def add_item1(request):
    if request.method == "POST":
        form = Item1Form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = Item1Form()
        return render(request, 'add_new.html', {'form': form})


def add_item2(request):
    if request.method == "POST":
        form = Item2Form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = Item2Form()
        return render(request, 'add_new.html', {'form': form})


def add_item3(request):
    if request.method == "POST":
        form = Item3Form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = Item3Form()
        return render(request, 'add_new.html', {'form': form})


def edit_item1(request, pk):
    item = get_object_or_404(Item1, pk=pk)

    if request.method == "POST":
        form = Item1Form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Item1Form(instance=item)

        return render(request, 'edit_item.html', {'form': form})


def edit_item2(request, pk):
    item = get_object_or_404(Item2, pk=pk)

    if request.method == "POST":
        form = Item2Form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Item2Form(instance=item)

        return render(request, 'edit_item.html', {'form': form})


def edit_item3(request, pk):
    item = get_object_or_404(Item3, pk=pk)

    if request.method == "POST":
        form = Item3Form(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Item3Form(instance=item)

        return render(request, 'edit_item.html', {'form': form})


def delete_item1(request, pk):
    template = 'index.html'
    Item1.objects.filter(id=pk).delete()

    items = Item1.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_item2(request, pk):
    template = 'index.html'
    Item2.objects.filter(id=pk).delete()

    items = Item2.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_item3(request, pk):
    template = 'index.html'
    Item3.objects.filter(id=pk).delete()

    items = Item3.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
