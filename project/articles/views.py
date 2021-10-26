from django.shortcuts import render
from articles.models import Article
# Create your views here.

def article_detail_view(request, id):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }

    return render(request, "articles/details.html" , context=context)