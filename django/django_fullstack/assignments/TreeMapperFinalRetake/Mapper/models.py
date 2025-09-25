import datetime
from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    # Registration validation
    def user_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')

        # First name
        if not post_data.get('first_name'):
            errors['first_name'] = "First name is required."
        elif len(post_data['first_name']) < 2:
            errors['first_name_short'] = "First name must be at least 2 characters."

        # Last name
        if not post_data.get('last_name'):
            errors['last_name'] = "Last name is required."
        elif len(post_data['last_name']) < 2:
            errors['last_name_short'] = "Last name must be at least 2 characters."

        # Email
        if not post_data.get('email'):
            errors['email_empty'] = "Email is required."
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['invalid_email'] = "Email format is not valid."
        elif self.model.objects.filter(email=post_data['email']).exists():
            errors['email_exists'] = "This email is already registered before."

        # Password
        if not post_data.get('password') or not post_data.get('confirm_pw'):
            errors['password'] = "Password and Confirm Password are required."
        elif len(post_data['password']) < 8:
            errors['short_password'] = "Password must be at least 8 characters."
        elif post_data['password'] != post_data['confirm_pw']:
            errors['password_match'] = "Passwords do not match."

        # check birthday - (must be at least 13 years old)
        if not post_data.get('birthday'):
            errors['birthday'] = "Birthday is required."
        else:
            try:
                # Convert string to date object
                birthday = datetime.datetime.strptime(post_data['birthday'], '%Y-%m-%d').date()
                today = datetime.date.today()
                
                # Check if birthday is in the future
                if birthday > today:
                    errors['birthday_future'] = "Birthday cannot be in the future."
                else:
                    # Calculate age
                    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
                    
                    # COPPA compliance 13...
                    if age < 13:
                        errors['birthday_underage'] = "You must be at least 13 years old to register!"
            except ValueError:
                errors['birthday_invalid'] = "Please enter a valid date."

        return errors

    # Login validation
    def user_login_validator(self, post_data):
        errors = {}

        email = post_data.get('email')
        password = post_data.get('password')

        if not email:
            errors['email_empty'] = "Email is required."
        elif not self.model.objects.filter(email=email).exists():
            errors['no_user'] = "User not found."
        else:
            user = self.model.objects.get(email=email)
            if not bcrypt.checkpw(password.encode(), user.password.encode()):
                errors['invalid_password'] = "Incorrect password."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=255)  # store hashed password later on
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


# Create your models here.
class ZipCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.code}"

class Tree(models.Model):
    species = models.CharField(max_length=255)
    notes = models.TextField(max_length=50)
    created_by = models.ForeignKey(User, related_name = "creates", on_delete = models.CASCADE) # the user who created a given tree
    date_found = models.DateField()
    location = models.CharField(max_length=255) # could be an address or coordinates
    zip_code = models.ForeignKey(ZipCode, related_name="trees", on_delete = models.CASCADE) # Zip codes where the tree is found
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.species} created by {self.created_by.first_name} {self.created_by.last_name}"

class Visit(models.Model):
    user = models.ForeignKey(User, related_name="visits", on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, related_name="visits", on_delete=models.CASCADE)
    date_visited = models.DateField(auto_now_add=True)
    
    # this stop user from re-visit and count it's as a visit 
    class Meta:
        unique_together = ('user', 'tree')

    def __str__(self):
        return f"{self.user.first_name} visited {self.tree.species}"
