from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Post,Reply
# from django.core.context_processors import request
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    username = request.user
    return render(request,'base.html',{'user':username})

def postform(request):
    posts = Post.objects.all().order_by('-posted_date')
    replys = Reply.objects.all().order_by('-posted-date')
    for rep in posts:
        reply = list(Reply.objects.filter(post==rep))
        rep.reply = reply 
        print rep.reply

    return render(request, 'post-reply.html', {'posts':posts})

@csrf_exempt
def addpost(request):
    # print"welcome"
    if request.method == "POST":
        data = request.POST['post-data']
        post = Post(post=data, user = request.user, posted_date = timezone.now(), updated = timezone.now())
        post.save()
        return HttpResponse("True")
    return HttpResponse("False")

def getdata(request):
    posts = Post.objects.all().order_by('posted-data')
    for rep in posts:
        reply = list(Reply.objects.filter(post = rep))
        rep.reply = reply 
    html = render_to_string('postrender.html',{'posts': posts})
    return HttpResponse(html)
