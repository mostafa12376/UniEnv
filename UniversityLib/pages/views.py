from django.shortcuts import render
from .models import Account, Book, Borrow
from django.contrib.auth.models import User, Permission
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.utils import timezone

def home(request):
    books = Book.objects.all()
    count = Book.objects.all().count()
    full=count
    last=0
    count=min(count,5)
    if count != 0:
        last=books[full-1]
        books=books[(full-count):full-1]

    return render(request, 'pages/Home_page.html',{'books':books,'last':last,'count':count})


def signin(request):
    if request.method=="POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        count=1
        return render(request, 'pages/signin.html',{'count':count})
    return render(request, 'pages/signin.html')

def signup(request):
    count=0
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['confirmPassword']
        userType = request.POST['userType']
        exist=User.objects.filter(username__exact=username).count()
        if exist==0:
            if password == Cpassword:
                if userType == 'user':
                    user = User.objects.create_user(username , email, password, is_staff = False,
                    is_active = True, is_superuser = False)
                    user.save()
                    acc = Account(user= user)
                    acc.save()
                    login(request,user)
                    return redirect('home')
                else:
                    user = User.objects.create_user(username, email, password, is_staff = True,
                    is_active = True, is_superuser = False)
                    permission = Permission.objects.get(codename = 'change_book')
                    user.user_permissions.add(permission)
                    user.save()
                    acc = Account(user= user)
                    acc.save()
                    login(request,user)
                    return redirect('home')

        else:
            count=1
    return render(request, 'pages/signup.html',{'count':count})




def Logout(request):
    logout(request)
    return redirect('home')




def editUserInfo(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            password = request.POST['password']
            email    = request.POST['email']
            user = request.user
            user.email   = email
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        return redirect('home')
    return render(request,'user/Edit.html')





def BrowseBooks(request):
    if request.user.is_authenticated:
        books = Book.objects.all()
        choices = ('Fantasy','Sci-fi','Mystery','Programming Language',
        'Autobiography','Historical','Technologies','Guide / How-to',
        'Families & Relationships')
        if request.method=='POST':
            name = request.POST.get('ISBN')
            acc = Account.objects.get(user__exact=request.user.id)
            theBook = Book.objects.get(ISBN__exact=name)
            x=Borrow.objects.filter(account__exact=acc, book__exact=theBook).exists()
            y= Borrow.objects.filter(book__exact=theBook).count()

            if not x and theBook.copies>y:

                borrow = Borrow(account=acc, book=theBook,borrowStartDate=timezone.now())
                borrow.save()
                return render(request,'pages/browseBooks.html',{'books':books,'choices':choices})
            else:

                return render(request,'pages/browseBooks.html',{'books':books,'choices':choices})

        else:
            booksSearch=request.GET.get('booksSearch')
            crt= request.GET.get('crt')
            cat= request.GET.get('cat')

            if cat != "ALL" and cat != None:

                books = Book.objects.filter(category__exact=cat)

            if booksSearch != None:
                if crt == "1":
                    books = books.filter(title__contains=booksSearch)
                elif crt == "2":
                    books = books.filter(author__contains=booksSearch)
                elif crt == "3":
                    books = books.filter(ISBN__exact=booksSearch)
                elif crt == "4":
                    books = books.filter(pubYear__exact=booksSearch)
            count = books.count()
            return render(request,'pages/browseBooks.html',{'books':books,'choices':choices,'count':count})
    else:
        return redirect('home')


def addBook(request):
    if request.user.is_authenticated and request.user.is_staff:
        choices = ('Fantasy','Sci-fi','Mystery','Programming Language',
        'Autobiography','Historical','Technologies','Guide / How-to',
        'Families & Relationships')
        if request.method =='POST':
            title = request.POST.get('title')
            author = request.POST.get('author')
            pubYear = request.POST.get('PubYear')
            ISBN = request.POST.get('ISBN')
            type = request.POST.get('type')
            copy = request.POST.get('copy')
            book = Book(title=title,author=author,ISBN=ISBN,pubYear=pubYear,category=type,copies=copy)
            book.save()
            return render(request,'pages/addBook.html',{'choices':choices})
        else:
            return render(request,'pages/addBook.html',{'choices':choices})
    else:
        return redirect('home')




def borrowedBooks(request):
    acc = Account.objects.get(user__exact=request.user.id)
    borrowed =Borrow.objects.filter(account__exact=acc)

    if request.method=='POST':
        extend = request.POST.get('extend')
        returned =  request.POST.get('return')


        if extend != None:
            book = Borrow.objects.get(account__exact=acc, book__ISBN__exact=extend)
            extandDays = request.POST.get('number')
            if (book.borrowPeriod+int(extandDays)) < 30:
                book.borrowPeriod+=int(extandDays)
            book.save()

        else:
            book = Borrow.objects.get(account__exact=acc, book__ISBN__exact=returned)
            book.delete()
            borrowed =Borrow.objects.filter(account__exact=acc)
    return render(request,'pages/borrowedBooks.html',{'borrowed':borrowed})
