from django.db import models

# Create your models here.

class BookStore(models.Model):
    id=models.IntegerField(primary_key=True)
    bookName=models.CharField(max_length=30)
    author=models.CharField(max_length=20)
    gener=(
        ('Mystery','Mystery'),('Thriller','Thriller'),('Comedy','Comedy'),('Horror','Horror')
        )
    category=models.CharField(max_length=30,choices=gener)
    first_pub=models.DateTimeField(auto_now_add=True)
    last_pub=models.DateTimeField(auto_now=True)