from rest_framework import serializers
from .models import Author, Genre, Book


#class AuthorSerializer(serializers.HyperlinkedModelSerializer):
class AuthorSerializer(serializers.ModelSerializer):
    """Класс-сериализатор, используемый для преобразования объектов модели Author в формат json"""

    class Meta:
        model = Author
        fields = ["firstname", "lastname", "birthdate", "deathdate"]


#class GenreSerializer(serializers.HyperlinkedModelSerializer):
class GenreSerializer(serializers.ModelSerializer):
    """Класс-сериализатор, используемый для преобразования объектов модели Genre в формат json"""

    class Meta:
        model = Genre
        fields = ["name"]


#class BookSerializer(serializers.HyperlinkedModelSerializer):
class BookSerializer(serializers.ModelSerializer):
    """Класс-сериализатор, используемый для преобразования объектов модели Book в формат json"""
    
    class Meta:
        model = Book
        fields = ["title", "author", "shortdescription", "genre", "isbn"]
