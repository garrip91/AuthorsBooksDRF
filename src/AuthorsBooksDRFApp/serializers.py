from .models import Author, Genre, Book
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """Класс-сериализатор, используемый для преобразования объектов модели Author в формат json"""
    
    class Meta:
        model = Author
        fields = ["firstname", "lastname", "birthdate", "deathdate"]


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """Класс-сериализатор, используемый для преобразования объектов модели Genre в формат json"""
    
    class Meta:
        model = Genre
        fields = ["name"]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    """Класс-сериализатор, используемый для преобразования объектов модели Book в формат json"""
    
    class Meta:
        model = Book
        fields = ["title", "author", "shortdescription", "genre", "isbn"]
