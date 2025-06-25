from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Post, Reply
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

def home(request):
    username = request.user
    return render(request, 'base.html', {'user': username})

def postform(request):
    posts = Post.objects.all().order_by('-posted_date')
    for rep in posts:
        reply = list(Reply.objects.filter(post=rep))
        rep.reply = reply
       
    return render(request, 'post-reply.html', {'posts': posts})

@csrf_exempt
def addpost(request):
    if request.method == "POST":
        data = request.POST['post_data']
        post = Post(post=data, user=request.user, posted_date=timezone.now(), updated=timezone.now())
        post.save()
        return HttpResponse("True")
    return HttpResponse("False")

def getdata(request):
    posts = Post.objects.all().order_by('-posted_date')
    for rep in posts:
        reply = list(Reply.objects.filter(post=rep))
        rep.reply = reply
    html = render_to_string('postrender.html', {'posts': posts})
    return HttpResponse(html)
@csrf_exempt
def addreply(request):
    if request.method == "POST":
        data = request.POST['reply_data']
        data_id = request.POST['postid']
        repost = Post.objects.get(id= int (data_id))
        reply = Reply(user = request.user, post = repost, reply= data, posted_date = timezone.now())
        reply.save()
        return HttpResponse("True")
    return HttpResponse("False")

