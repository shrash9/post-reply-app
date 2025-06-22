from django.shortcuts import render

# Create your views here.
def home(request):
    username = request.user
    return render(request,'base.html',{'user':username})
