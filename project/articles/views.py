from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from articles.models import Article
from django.contrib.auth.decorators import login_required
from articles.forms import ArticleForm
# Create your views here.

# @login_required
# def article_create_view(request):
#     context = {"form": ArticleForm}
#     form = ArticleForm(request.POST or None)
#     context['form'] = form
#     if form.is_valid():
#         title = form.cleaned_data.get('title')
#         content = form.cleaned_data.get('content')
#         print(title,content)
#         article_object = Article.objects.create(title=title,content=content)
#         context['object'] = article_object
#         context['created'] = True
#     return render(request,"articles/create.html",context=context)

@login_required
def article_create_view(request):
    context = {"form": ArticleForm}
    form = ArticleForm(request.POST or None)
    context['form'] = form
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()  # clean the form avoid post dublicate articles
        context['object'] = article_object
        context['created'] = True
    return render(request,"articles/create.html",context=context)

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