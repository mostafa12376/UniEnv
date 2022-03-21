from django.urls import path
from . import views

urlpatterns = [
    path('Signup',views.signup,name='signup') ,
    path('Signin',views.signin,name='signin'),
    path('',views.home,name='home'),
    path('user/edit', views.editUserInfo, name= 'edit'),
    path('browsebooks/',views.BrowseBooks,name='browseBooks'),
    path('logout/',views.Logout,name='logout'),
    path('addbook/',views.addBook,name='addBook'),
    path('borrowedbooks/',views.borrowedBooks,name='borrowedBooks'),

]
