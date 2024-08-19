from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache
@receiver(user_logged_in,sender = User)
def login_success(sender,request,user,**kwargs):
    # we will store login count in cache
    # we add version because every user's login should be distinct
    curr = cache.get('count',0,version = user.pk)
    cache.set('count',curr + 1,24 * 60 * 60,version= user.pk)
    print(user.pk)
