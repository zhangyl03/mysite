from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogsPost
 
# Create your views here.
 
def index(request):
    posts = BlogsPost.objects.all()
    t = loader.get_template("index.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))