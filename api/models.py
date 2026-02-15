from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    """
    Author Model
    ------------
    Represents a book author.

    Fields:
    - name: Stores the full name of the author.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book Model
    ----------
    Represents a book written by an Author.

    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: ForeignKey linking to Author (one-to-many relationship).
              One Author can have multiple Books.
    """

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    # One-to-many relationship:
    # An author can have many books
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title
