from django.shortcuts import render, HttpResponse


# Create your views here.

def article_list(request):
    article = "This is my first article title"
    return render(request, 'articles.html', {'article':article})
