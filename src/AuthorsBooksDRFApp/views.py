from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Author, Genre, Book


# class IndexView(TemplateView):
#     #template_name = "AuthorsBooksDRFApp/index.html"
#     template_name = "index.html"
#    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         #context["title"] = "Home - Главная"
#         #context["content"] = "Магазин мебели HOME"
#         return context


def index(request):
    
    authors = Author.objects.all()
    genres = Genre.objects.all()
    books = Book.objects.all()
    
    zipped_data = zip(authors, books)
    zipped_data_list = list(zipped_data)
    print(zipped_data_list)
    context = {
        "zipped_data": zipped_data_list,
        "genres": genres,
    }
    
    return render(request, "index.html", context)
