from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from ztq.models import Book
from ztq.models import Movietreu
from django.core.paginator import Paginator
# Create your views here.
def show(request,num):
    li=Book.objects.all()[:100]
    pgs=Paginator(li,10)
    if(num>pgs.num_pages):
        return render(request, 'show.html', {"ls": pgs.page(pgs.num_pages)})
    if (num<=1):
        return render(request, 'show.html', {"ls": pgs.page(1)})
    return render(request, 'show.html',{"ls":pgs.page(num)})

def movie(request,num):
    li=Movietreu.objects.all()[:100]
    pgs=Paginator(li,10)
    if(num>pgs.num_pages):
        return render(request, 'movie.html', {"ls": pgs.page(pgs.num_pages)})
    if (num<=1):
        return render(request, 'movie.html', {"ls": pgs.page(1)})
    return render(request, 'movie.html',{"ls":pgs.page(num)})


