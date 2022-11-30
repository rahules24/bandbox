# from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Item, Slip
import math


def index(request):
    allitems = []
    # slipid = []
    # slipids = Slip.objects.values('slip_id')
    # ids = {item['slip_id'] for item in slipids}
    catitems = Item.objects.values('category')
    cats = {item['category'] for item in catitems}
    for cat in cats:
        item = Item.objects.filter(category=cat)
        allitems.append(item)
    # for i in ids:
    #     num = Slip.objects.filter(slip_id=i)
    #     slipid.append(num)
    # # print(slipid)
    return render(request, 'index.html', {'allitems': allitems})
