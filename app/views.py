from django.shortcuts import render

# Create your views here.

def user_defined_filters(request):
    d={'usd':'hai python how are you'}
    return render(request,'user_defined_filters.html',d,)