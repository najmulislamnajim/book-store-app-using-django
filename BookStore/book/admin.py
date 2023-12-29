from django.contrib import admin
from book.models import BookStore

# Register your models here.

class BookStoreAdmin(admin.ModelAdmin):
    list_display=['id','bookName','author','category','first_pub','last_pub']
    
admin.site.register(BookStore,BookStoreAdmin)