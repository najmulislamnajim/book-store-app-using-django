from django.urls import path
from book.views import form,books,edit,delete

urlpatterns = [
    path('',books,name='books'),
    path('form/',form,name='form'),
    path('edit/<int:id>',edit,name='edit'),
    path('delete/<int:id>',delete,name='delete'),
]
