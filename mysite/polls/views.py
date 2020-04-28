from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You are in the polls index.")

def geeks_view(request): 
    # render function takes argument  - request 
    # and return HTML as response 
    return render(request, "home.html") 


