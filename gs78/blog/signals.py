from django.dispatch import Signal,receiver

#creating Signals
notification = Signal()

#Receiver Function
@receiver(notification)
def show_notification(sender,**kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")