from django.db import models
from django.contrib import admin
#from myproject.myapp.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    def __unicode__ (self):
        return self.title

class Comment(models.Model):
    body=models.TextField()
    author=models.CharField(max_length=60)
    created=models.DateField(auto_now=True)
    update=models.DateField(auto_now=True)
    post=models.ForeignKey(Post)
    def __unicode__ (self):
        return self.author
    def first_60(self):
        return self.title[:60]



class PostAdmin(admin.ModelAdmin):
    list_display=('title','created','updated')
    search_fields=('title','body')
    list_filter=('created')
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author','first_60','date created','date updated')
    list_filter=('created','author')
    
    
    

class CommentInline(admin.TabularInline):
    model=Comment
class AuthorAdmin(admin.ModelAdmin):
    inlines=[CommentInline]
    
admin.site.register(Post)
admin.site.register(Comment)
  
    
