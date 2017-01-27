from django.shortcuts import render, redirect
from .models import User, Wishlist
from django.contrib import messages

# Create your views here.
def dashboard(request):
    if "id" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    users = User.objects.all()
    items = Wishlist.objects.all()
    context = {'user': user,
                'users': users,
                'items': items }
    print request.session['id']
    return render(request, "index.html", context)

def item(request, id):
    curItem = Wishlist.objects.get(id=id)
    items = Wishlist.objects.all()
    users = User.objects.all()
    hasItems = Wishlist.objects.select_related().filter(id=id)
    print hasItems
    context = { 'items': items,
                'users': users,
                'curItem': curItem,
                'itemid': id,
                'hasItems': hasItems }
    return render(request, "item.html", context)

def add(request):
    return render(request, "add.html")

def create(request):
    errors = Wishlist.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('/wishlist/add')
    user = User.objects.get(id=request.session['id'])
    user.wishlist_set.create(name=request.POST['name'])
    return redirect('/wishlist/dashboard')

def remove(request):
    item = Wishlist.objects.get(id=request.POST['id'])
    item.delete()
    return redirect('/wishlist/dashboard')


def createById(request, id):
    item = Wishlist.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.wishlist_set.create(name=item.name)
    Wishlist.objects.filter(id=id).delete()
    return redirect('/wishlist/dashboard')

def delete(request, id):
    Wishlist.objects.filter(id=id).delete()
    return redirect('/wishlist/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')
