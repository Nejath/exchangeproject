from django.shortcuts import render
from shop.models import Products,Category
from cart.models import Liked
from shop.forms import Productform
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    i=Products.objects.all().order_by('-updated')

    return render(request,'home.html',{'items':i})

def category_based_products(request,s):
    c=Category.objects.get(slug=s)
    p=Products.objects.filter(category__slug=s)
    return render(request, 'category_products.html', {'p':p,'c':c})


@login_required
def item_details(request,p):

    d = Products.objects.get(id=p)
    l=[]
    like=None
    user = request.user
    try:
        like = Liked.objects.get(user=user, products=d)
    except Liked.DoesNotExist:
        pass

    if(d.image1):
        l.append(d.image1)
    if (d.image2):
        l.append(d.image2)
    if (d.image3):
        l.append(d.image3)

    return render(request, 'item_details.html', {'d': d,'l':l,'like':like})


@login_required
def add_items(request):
    form=Productform()
    u=request.user
    if(request.method=="POST"):
        form=Productform(request.POST,request.FILES)
        if form.is_valid():
            p=form.save(commit=False)
            p.user=u
            p.save()
            return home(request)
    return render(request, 'add_items.html',{'form':form} )


# @login_required()
# def add_items(request):
#     user=request.user
#
#     if (request.method == "POST"):
#         c = request.POST['c']
#         slug=Category.objects.get(slug=c)
#         n = request.POST['n']
#         d = request.POST['d']
#         pr = request.POST['pr']
#         pl = request.POST['pl']
#         m = request.POST['m']
#         i1 = request.FILES.get('i1')
#         i2 = request.FILES.get('i2')
#         i3 = request.FILES.get('i2')
#         p = Products.objects.create(user=user,category=slug,name=n,description=d,price=pr,address=pl,phone=m,)
#         if (i1):
#             p.image1=i1
#         if (i2):
#             p.image2=i2
#         if (i3):
#             p.image3=i3
#         p.save()
#         return home(request)
#     return render(request,'add_items.html')

@login_required()
def your_items(request):
    user=request.user
    try:
        items=Products.objects.filter(user=user)
    except:
        pass

    return render(request,'your_items.html',{'items':items})



@login_required
def update_your_item(request,p):
    b = Products.objects.get(id=p)
    form = Productform(instance=b)
    if (request.method == "POST"):
        form = Productform(request.POST,request.FILES,instance=b)

        if form.is_valid():
            form.save()
            return your_items(request)
    return render(request, 'update_your_item.html', {'form': form})

@login_required
def remove_your_item(request,p):
    b = Products.objects.get(id=p)
    b.delete()
    return your_items(request)


