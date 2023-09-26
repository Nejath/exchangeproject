from django.shortcuts import render
from shop.models import Products,Category
from django.db.models import Q



def searchresult(request):
    query=""
    r=None
    if(request.method=="POST"):
        query=request.POST.get('q')
        if(query):
            r=Products.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) | Q(address__icontains=query) | Q(category__name__icontains=query))
    return render(request,'search.html',{'query':query,'result':r})

