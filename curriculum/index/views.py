from django.shortcuts import render,HttpResponse

# Create your views here.
def Curriculum(request):
    return render(request,"CV.html")

def hub(requet):
    return HttpResponse("Server ON")