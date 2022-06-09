from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help='run in order to join darth handle'
    
    def handle(self,*args,**kargs):
        print('Please Like,Comment,Subscribe')