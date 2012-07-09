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
    result=Post.objects.get(pk=id)
    html=''
    for i in result.comment.all():
        html+=str(i)
    return HttpResponse(str(result)+'<br/>'+ str(result.body)+'<br/>'+ html)
    
def post_search(request, term):
    result = re.search(r'.*',term)
    
    return HttpResponse(result)
    

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
