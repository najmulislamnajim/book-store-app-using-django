from django.shortcuts import render,redirect
from book.forms import Bookstore
from book.models import BookStore

# Create your views here.

def form(request):
    
    if request.method=='POST':
        book=Bookstore(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
            book.save()
            return redirect('books')
    else:
        book=Bookstore()
    return render(request,'add_books.html',{'form':book})

def books(request):
    book=BookStore.objects.all()
    return render(request,'show_books.html',{'books':book})


def edit(request,id):
    book=BookStore.objects.get( pk = id )
    form=Bookstore(instance=book)
    
    if request.method=='POST':
        book=Bookstore(request.POST,instance=book)
        if book.is_valid():
            book.save()
            return redirect('books')
        
    return render(request,'add_books.html',{'form':form})


def delete(request,id):
    book=BookStore.objects.get(pk=id).delete()
    return redirect('books')