from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Author, Genre, Book
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer


# class IndexView(TemplateView):
#     #template_name = "AuthorsBooksDRFApp/index.html"
#     template_name = "index.html"
#    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         #context["title"] = "Метатег <title>"
#         #context["content"] = "Метатег <content>"
#         return context


def index(request):
    """Функция представления для основной страницы с авторами и их книгами"""
    
    authors = Author.objects.all()
    genres = Genre.objects.all()
    books = Book.objects.all()
    
    zipped_data = zip(authors, books) # упаковываем модель авторов и модель книг в zip() для их совместного отображения в одной видимой таблице на странице index.html
    zipped_data_list = list(zipped_data) # преобразуем наш zip() в список для лучшего отображения в консоли
    print(zipped_data_list) # отображаем наш полученный список в консоли 
    
    context = {
        "zipped_data": zipped_data_list,
        "genres": genres,
    }
    
    return render(request, "index.html", context)


class AuthorViewSet(viewsets.ModelViewSet):
    """Класс обработки запросов и возврата ответов ДЛЯ АВТОРОВ с их последующей передачей на соответствующую страницу (в данном случае это localhost/authors/)"""
    
    queryset = Author.objects.all().order_by("id")
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenreViewSet(viewsets.ModelViewSet):
    """Класс обработки запросов и возврата ответов ДЛЯ ЖАНРОВ с их последующей передачей на соответствующую страницу (в данном случае это localhost/genres/)"""
    
    queryset = Genre.objects.all().order_by("id")
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """Класс обработки запросов и возврата ответов ДЛЯ КНИГ с их последующей передачей на соответствующую страницу (в данном случае это localhost/books/)"""
    
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllDataView(APIView):
    """Класс обработки запросов и возврата ответов ДЛЯ ВСЕХ ОБЪЕКТОВ/СУЩНОСТЕЙ с их последующей передачей на соответствующую страницу (в данном случае это localhost/all-data/)"""
    
    def get(self, request):
        
        authors = Author.objects.all()
        genres = Genre.objects.all()
        books = Book.objects.all()
        
        author_serializer = AuthorSerializer(authors, many=True)
        genre_serializer = GenreSerializer(genres, many=True)
        book_serializer = BookSerializer(books, many=True)
        
        return Response({
            "authors": author_serializer.data,
            "genres": genre_serializer.data,
            "books": book_serializer.data,
        })
