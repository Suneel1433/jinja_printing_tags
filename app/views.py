from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'suneel devanboina'}
    return render(request,'wish.html',context=d)
