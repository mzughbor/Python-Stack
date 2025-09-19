from django.db import models
from user_login_app.models import User

# Create your models here.
class ZipCode(models.Model):
    code = models.CharField(max_length=5, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code}"

class Tree(models.Model):
    species = models.CharField(max_length=255)
    notes = models.TextField(max_length=50)
    uploaded_by = models.ForeignKey(User, related_name = "trees_uploaded", on_delete = models.CASCADE) # the user who uploaded a given tree
    date_found = models.DateField()
    location = models.CharField(max_length=255) # could be an address or coordinates
    users_who_visit = models.ManyToManyField(User, related_name = "visited_trees") # a list of visited users
    zip_codes = models.ForeignKey(ZipCode, related_name="trees", on_delete = models.CASCADE) # Zip codes where the tree is found
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.species} uploaded by {self.uploaded_by.first_name} {self.uploaded_by.last_name}"
