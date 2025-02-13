from django.contrib import admin

from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "birthdate", "deathdate"]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "shortdescription", "isbn"]
