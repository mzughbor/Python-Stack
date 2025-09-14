from django.db import models

# Create your models here.

class TVShowManager(models.Manager):
    
    def basic_validator(self, postData):        
        errors = {}
        from datetime import datetime, date
        
        # Title validation
        if len(postData['title']) < 2:
            errors["title"] = "Title input should be at least 2 characters!"
        else:
            # Check for duplicate titles, excluding the current show being edited by the flag show_id
            show_id = postData.get('show_id')
            exists = TVShow.objects.filter(title=postData['title'])
            if show_id:
                exists = exists.exclude(id=show_id)
            if exists:
                errors["title"] = f"A show with the title '{postData['title']}' already exists!"

        # Network validation
        if len(postData['network']) < 3:
            errors["network"] = "Network input should be at least 3 characters"
        
        # Release date validation
        try:
            release_date = datetime.strptime(postData['release_date'], '%Y-%m-%d').date()
            if release_date >= date.today():
                errors["release_date"] = "Release date must be in the past"
        except (ValueError, TypeError):
            errors["release_date"] = "Please enter a valid release date"
        
        # Description validation
        if postData['desc']:  # ? description is not empty
            if len(postData['desc']) < 10:
                errors["desc"] = "Description must be at least 10 characters when provided"
        
        return errors
        
        """
        descLen = len(postData['desc'])
        if descLen < 10:
            if descLen != 0:
                errors["desc"] = "Description(optional) should be at least 10 characters if entered or left empty"
        """

class TVShow(models.Model):
    title = models.CharField(max_length=255) # we can say unique=True and catch the IntegrityError about UNIQUE constraint failure
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TVShowManager()

    def __str__(self):
        return f'{self.title} ({self.network})'

