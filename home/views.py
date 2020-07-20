from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("this is homepage")  #it uses the string, when we want to retrn strung we use httpresponse
    return render(request,'index.html')
def about(request):
    # return HttpResponse("this is about page")
    return render(request, 'post.html')

def resume(request):
    # return HttpResponse("this is resume page we may see here resume")
    return render(request, 'resume.html')

def contact(request):
    # return HttpResponse("this is the way you contact to me") 
    return render(request, 'contact.html')
