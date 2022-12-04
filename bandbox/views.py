# from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Item, Slip


def index(request):
    allitems = []
    catitems = Item.objects.values('category')
    cats = {item['category'] for item in catitems}
    for cat in cats:
        item = Item.objects.filter(category=cat)
        allitems.append(item)
    return render(request, 'index.html', {'allitems': allitems})


def slip(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJSON', '')
        address = request.POST.get('address', '')
        amount = request.POST.get('amount', '')
        phone = request.POST.get('phone', '')
        date = request.POST.get('date', '')
        duedate = request.POST.get('due-date', '')
        newslip = Slip(items_json=items_json, amount=amount, address=address, phone=phone, date=date, due_date=duedate)
        newslip.save()
    return render(request, 'slip.html')
