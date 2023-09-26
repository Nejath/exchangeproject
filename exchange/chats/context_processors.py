
from chats.models import Conversation
def conv_noti(request):

    n=False
    if request.user.is_authenticated:
        u = request.user
        c = Conversation.objects.filter(participants=u).filter(notification=True)
        for i in c:
            if(i.latest_message.sender != u):
                n=True
                break
            else:
                pass
        else:
            pass

    return {'n':n}

