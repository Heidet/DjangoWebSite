from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def accueil(request):
#     message = "Hello World!"
#     return HttpResponse(message)

def accueil(request):
    """ Afficher les articles du blog """
    # articles = Article.objects.all()
    return render(request, 'store/home.html')

def presentation(request):
    """ Afficher les articles du blog """
    # articles = Article.objects.all()
    return render(request, 'store/presentation.html')

