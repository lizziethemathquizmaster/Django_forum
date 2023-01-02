from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import Post
from .forms import PostForm 

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())    
    posts = Post.objects.all()[:20]

    return render(request, 'posts.html',
                        {'posts':posts})

def delete(request, post_id):
    output = 'POST ID is ' + str(post_id)
    return HttpResponse(output)                        
