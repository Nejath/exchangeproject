from django.shortcuts import render,redirect
from chats.models import Message,Conversation
from shop.models import Products,Category
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def messagebox(request,p,item_id=None):
    item = None
    if item_id:
       item=Products.objects.get(id=item_id)
    m={}
    s=request.user
    r=User.objects.get(id=p)
    conv=Conversation.objects.filter(participants=s).filter(participants=r).first()
    if conv:
        m=Message.objects.filter(conversation=conv).order_by('timestamp')
        if request.user != conv.latest_message.sender:
            conv.notification=False
            conv.save()

    if(request.method=="POST"):
        if conv:
            msg = request.POST['msg']
            message=Message.objects.create(content=msg,sender=request.user,conversation=conv)
            message.save()
            conv.latest_message = message
            conv.message_count += 1
            conv.notification = True
            conv.save()
            if item:
                return redirect('chats:messagebox',r.id,item.id)
            else:
                return redirect('chats:messagebox', r.id)

        else:

            c = Conversation.objects.create()
            c.participants.add(s,r)
            msg = request.POST['msg']
            message = Message.objects.create(content=msg, sender=request.user, conversation=c)
            message.save()
            c.latest_message = message
            c.message_count += 1
            c.notification = True
            c.save()
            if item:
                return redirect('chats:messagebox',r.id,item.id)
            else:
                return redirect('chats:messagebox', r.id)

    return render(request, 'messagebox.html',{'m':m,'r':r,'item':item} )

@login_required
def yourchats(request):
    u=request.user
    c = Conversation.objects.filter(participants=u).order_by('-latest_message')
    return render(request, 'yourchats.html',{'c':c} )