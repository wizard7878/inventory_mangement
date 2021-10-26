from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article



def article_home_view(request):
    return HttpResponse

def home_view(request , id = None, *args , **kwargs):

    articles = Article.objects.all()

    html = render_to_string("home-view.html",context={"id":1,"title":"Hello","content":"world","articles":articles})
    return HttpResponse(html)