from django.db import models
from django.http import JsonResponse

# Create your models here.

class TVShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        from datetime import datetime, date

        # Title validation
        if len(postData.get('title', '')) < 2:
            errors["title"] = ["Title must be at least 2 characters long."]
        else:
            # Check duplicates
            show_id = postData.get('show_id')
            exists = TVShow.objects.filter(title=postData['title'])
            if show_id:
                exists = exists.exclude(id=show_id)
            if exists:
                errors["title"] = [f"A show with the title '{postData['title']}' already exists!"]

        # Network validation
        if len(postData.get('network', '')) < 3:
            errors["network"] = ["Network must be at least 3 characters long."]

        # Release date validation
        try:
            release_date = datetime.strptime(postData.get('release_date', ''), '%Y-%m-%d').date()
            if release_date >= date.today():
                errors["release_date"] = ["Release date must be in the past."]
        except (ValueError, TypeError):
            errors["release_date"] = ["Please enter a valid release date."]

        # Description validation
        desc = postData.get('desc', '')
        if desc and len(desc) < 10:
            errors["desc"] = ["Description must be at least 10 characters when provided."]

        return errors  # ✅ return dict only, no JsonResponse


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

