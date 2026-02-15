from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer
    --------------
    Serializes all fields of the Book model.

    Includes custom validation to ensure
    publication_year is not in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation:
        Ensures publication year is not in the future.
        """
        current_year = datetime.date.today().year

        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )

        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer
    ----------------
    Serializes Author model including nested books.

    The 'books' field uses BookSerializer
    to dynamically serialize all books written
    by this author.

    Relationship handling:
    - Uses related_name='books' from the Book model.
    - many=True because one author can have multiple books.
    - read_only=True prevents direct book creation from this serializer.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
