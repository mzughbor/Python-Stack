from django.db import models
from user_login_app.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name = "books_uploaded", on_delete = models.CASCADE) # the user who uploaded a given book
    users_who_like = models.ManyToManyField(User, related_name = "liked_books") # a list of users
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} uploaded by {self.uploaded_by.first_name} {self.uploaded_by.last_name}"
