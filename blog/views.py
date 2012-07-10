# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    print type(post_list)
    print post_list
    return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
    result=Post.objects.all()[int(id)-1]
    html=''
    for i in result.comment.all():
        html+=str(i.body)+'<br/>'
    return HttpResponse('<li>'+str(result) + '<h5/>''<br/>' + result.body +
                        '<h5/>'+'<br/>'+'<p>'+html)
    
    
def post_search(request, term):
    result=Post.objects.filter(body__contains=term)
    response=''
    for j in result:
        response+=str(j)+'<br/>'
    return HttpResponse(str(response))
    

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
