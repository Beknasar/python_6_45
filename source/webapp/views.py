from django.shortcuts import render
from webapp.models import Article
# Create your views here.
def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })

def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        print(request.POST)
        context = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author')
        }

        return render(request, 'article_view.html', context)