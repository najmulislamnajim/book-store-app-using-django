from django import forms
from book.models import BookStore 


class Bookstore(forms.ModelForm):
    class Meta:
        model=BookStore
        fields='__all__'
        labels={'bookName':'Book Name','author':'Author','category':'Category','first_pub':'First Publication','last_pub':'Last Publication'}
        