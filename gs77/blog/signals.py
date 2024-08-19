from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created

# @receiver(user_logged_in,sender = User)
# def login_success(sender,request,user,**kwargs):
#     print("-------------------------------")
#     print("Logged-in Signal... Run Intro")
#     print("Sender:",sender)
#     print("Request",request)
#     print("User",user)
#     print(f'kwargs:{kwargs}')


'''
connecting the singal with recevier
using manual connect route method
'''
#user_logged_in.connect(login_success,sender = User)
@receiver(user_logged_out,sender = User)
def logout(sender,request,user,**kwargs):
    print("-------------------------------")
    print("Logged-out Signal... Run Outro")
    print("Sender:",sender)
    print("Request",request)
    print("User",user)  
    print(f'kwargs:{kwargs}')
#user_logged_out.connect(login_success,sender = User)



@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("-------------------------------")
    print("Login Failed Signal...   ")
    print("Sender:",sender)
    print("Request",request)
    print("Credentials:",credentials)  
    print(f'kwargs:{kwargs}')
#user_login_failed.connect(login_failed)


@receiver(pre_save,sender = User)
def at_beginning_save(sender,instance,**kwargs):
    print("Sender:",sender)
    print("Instance",instance)

    print(f'kwargs:{kwargs}')

@receiver(post_save,sender = User)
def after_save(sender,instance,created,**kwargs):
    if created:

        print("-------------------------------")
        print("Post save singal")
        print("Sender:",sender)
        print("New Record")
        print("Instance",instance)
        print("Created:",created)

        print(f'kwargs:{kwargs}')
    else:
        print("-------------------------------")
        print("Updated")
        print("Post save singal")
        print("Sender:",sender)
        print("Instance",instance)

        print(f'kwargs:{kwargs}')


@receiver(pre_delete,sender = User)
def at_beginning_delete(sender,instance,**kwargs):
    print("-------------------------------")
    print("Pre Delete singal")
    print("Sender:",sender)
    print("New Record")
    print("Instance",instance)
    

    print(f'kwargs:{kwargs}')

@receiver(post_delete,sender = User)
def after_delete(sender,instance,**kwargs):
    print("-------------------------------")
    print("Post Delete singal")
    print("Sender:",sender)
    print("New Record")
    print("Instance",instance)



@receiver(pre_init,sender = User)
def at_beginning_init(sender,*args,**kwargs):
    print("-------------------------------")
    print("Pre Init signal")
    print("Sender:",sender)
    print(f'Args:{args}')
    print(f'kwargs:{kwargs}')


@receiver(pre_init,sender = User)
def at_post_init(sender,*args,**kwargs):
    print("-------------------------------")
    print("Post Init signal")
    print("Sender:",sender)
    print(f'Args:{args}')
    print(f'kwargs:{kwargs}')


@receiver(request_started)
def at_beginning_request(sender,environ,**kwargs):
    print("-------------------------------")
    print("At beginning request")
    print("Sender:",sender)
    print("Environ:",environ)
    print(f'kwargs:{kwargs}')
#request_started.connect(at_beginning_request)

@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("-------------------------------")
    print("At ending request")
    print("Sender:",sender)
    print(f'kwargs:{kwargs}')
#request_started.connect(at_ending_request)

@receiver(got_request_exception)
def at_req_exception(sender,request,**kwargs):
    print("-------------------------------")
    print("At req Exception")
    print("Sender:",sender)
    print("Request:",request)
    print(f'kwargs:{kwargs}')
#request_started.connect(at_ending_request)


@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print("-------------------------------")
    print("At req Exception")
    print("Sender:",sender)
    print("connection:",connection)
    print(f'kwargs:{kwargs}')








