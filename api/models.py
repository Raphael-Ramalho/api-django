from django.db import models

# Create your database ORM models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100) # this is defining an small string field with limited length
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # def is creating an function and __str__ is an common way to return an string when class instance is called
        return self.title
