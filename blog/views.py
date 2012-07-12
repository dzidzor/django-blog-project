# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Post, Comment 


def post_list(request):
    posts = Post.objects.all()
    temp = loader.get_template('blog/post_list.html')
    cont = Context({'posts':posts})
    return HttpResponse(temp.render(cont))

def post_detail(request, id, showComments=False):
    posts= Post.objects.get(pk=id)
    comments=Comment.objects.get(pk=id)
    temp= loader.get_template('blog/post_detail.html')
    cont = Context({'posts':posts,'comment':comments})
    return HttpResponse(temp.render(cont))
    #html=''
    #for i in result.comment.all():
     #   html+=str(i.body)+'<br/>'
    #return HttpResponse('<li>'+str(result) + '<h5/>''<br/>' + result.body +
     #                   '<h5/>'+'<br/>'+'<p>'+html)
    
    
def post_search(request, term):
    posts=Post.objects.filter(body__contains=term)
    temp= loader.get_template('blog/post_search.html')
    cont=Context({'posts':posts,'term':term})
    #result=Post.objects.filter(body__contains=term)
    #response=''
    #for j in result:
        #response+=str(j)+'<br/>'
    return HttpResponse(temp.render(cont))
    

def home(request):
    return render_to_response('blog/base.html',{}) 
