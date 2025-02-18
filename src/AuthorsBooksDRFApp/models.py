from django.db import models


class Author(models.Model):
    """Класс для таблицы с авторами"""
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    deathdate = models.DateField(default="Скончался", blank=True, null=True)
    
    class Meta:
        ordering = ("id",)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Genre(models.Model):
    """Класс для таблицы с жанрами"""
    
    name = models.CharField(max_length=200, help_text="Укажите здесь жанр книги")
    
    class Meta:
        ordering = ("id",)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    """Класс для таблицы с книгами"""
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    shortdescription = models.TextField(max_length=1000, help_text="Укажите здесь краткое описание книги")
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр для этой книги")
    isbn = models.CharField(default="ISBN", max_length=20, help_text="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9_%D0%BD%D0%BE%D0%BC%D0%B5%D1%80")
    
    class Meta:
        ordering = ("id",)
    
    def __str__(self):
        return self.title
