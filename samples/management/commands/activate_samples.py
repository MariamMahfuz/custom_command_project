from itertools import count
from django.core.management.base import BaseCommand
from samples.models import Samples

class  Command(BaseCommand):
    help='activate all inactive samples'

    def handle(self,*args,**kargs):
        size=Samples.objects.filter(activated=False).count()
        if size!=0:
            qs=Samples.objects.filter(activated=False)
            count=0
            for obj in qs:
                count+=1
                obj.activated=True
                obj.save()
            print(f"activated {count} objects")

        else:
            print("Nothing here to do")
