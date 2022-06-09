from ast import parse
from itertools import count
from sqlite3 import paramstyle
from tkinter import S
from django.core.management.base import BaseCommand
from samples.models import Samples

class  Command(BaseCommand):
    help='Multiply the total count by a param'

    def add_arguments(self, parser):
        parser.add_argument('param',type=int)

    def handle(self,*args,**options):
        param=options.get('param')
        count=Samples.objects.all().count()
        multiply=count*param
        print(multiply)

