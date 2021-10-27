from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from articles.models import Article
# Create your views here.

def article_search_view(request):
    print(request.GET)
    query_dict = request.GET
    article = None
    try:
        query = int(query_dict.get('query'))
        print(query)
    except:
        query = None
    if query is not None:
        article = Article.objects.get(id=query)
    context = {'object': article}
    return render(request,"articles/search.html" , context=context)

def article_detail_view(request, id):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }

    return render(request, "articles/details.html" , context=context)