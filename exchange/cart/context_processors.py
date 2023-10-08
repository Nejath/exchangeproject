
from .models import Liked

def like_counter(request):
    like_count = 0
    if request.user.is_authenticated:
        user = request.user
        try:
            likes = Liked.objects.filter(user=user)
            for i in likes:
                like_count += 1
        except:
            like_count = None
    return {'like_count': like_count}

