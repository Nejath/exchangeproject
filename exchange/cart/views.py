from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse
from shop.models import Category,Products
from cart.models import Liked


from django.contrib.auth.decorators import login_required


@login_required()
def likedview(request):
    liked=None
    user=request.user
    try:
        liked=Liked.objects.filter(user=user).order_by('-id')
    except Liked.DoesNotExist:
        pass
    return render(request,'likedview.html',{'liked':liked})

@login_required()
def like_unlike(request,p):
    product=Products.objects.get(id=p)
    user=request.user
    is_liked = False
    if request.headers.get('X_Requested-With') == 'XMLHttpRequest':
        try:
            like=Liked.objects.get(user=user,products=product)
            like.delete()
        except Liked.DoesNotExist:
            like=Liked.objects.create(user=user, products=product)
            like.save()
            is_liked = True
        return JsonResponse({'data':is_liked},)
    else:
        try:
            like=Liked.objects.get(user=user,products=product)
            like.delete()
        except Liked.DoesNotExist:
            like=Liked.objects.create(user=user, products=product)
            like.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

