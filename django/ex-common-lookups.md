# models.py

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} by {self.author.name}"



### Now some example queries using field lookups:

from datetime import date

# 1. All books whose title starts with "The"
Book.objects.filter(title__startswith="The")

# 2. All books by authors whose name contains "Orwell"
Book.objects.filter(author__name__contains="Orwell")

# 3. All authors born before year 1970
Author.objects.filter(birth_date__lt=date(1970,1,1))

# 4. All books published in the years 2000, 2005, 2010
Book.objects.filter(published_year__in=[2000, 2005, 2010])

# 5. All books where author name is exactly "J.K. Rowling", case-insensitive
Book.objects.filter(author__name__iexact="j.k. rowling")

# 6. All books where the author is null (if you allowed that)
Book.objects.filter(author__isnull=True)

