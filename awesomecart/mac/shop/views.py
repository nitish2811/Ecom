from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact,Orders,Orderupdate
from math import ceil
import json

def index(request):
     # products=Product.objects.all()

     # params={'product':products,'no_slide':nslide,'range':range(1,nslide)}
     # allProd=[[products,range(1,nslide),nslide],
     #          [products,range(1,nslide),nslide]]
     allProds=[]
     catprods=Product.objects.values('category','id')
     cats={item['category'] for item in catprods}
     for cat in cats:
          prod=Product.objects.filter(category=cat)
          n = len(prod)
          nslide = n // 4 + ceil((n / 4) - (n // 4))
          allProds.append([prod,range(1,nslide),nslide])

     params={'allProds':allProds}
     return render(request, 'shop/index.html', params)


def about(request):
     return render(request,'shop/about.html')

def test(request):
     return render(request,'shop/test.html')

def contact(request):
     if request.method=="POST":
          Name=request.POST.get('name','')
          email=request.POST.get('email','')
          phone=request.POST.get('phone','')
          desc=request.POST.get('texta','')
          cont=Contact(name=Name,email=email,phone=phone,desc=desc)
          cont.save()


     return render(request, 'shop/Contact.html')

def tracker(request):
     if request.method == "POST":
          orderid = request.POST.get('orderid', '')
          city = request.POST.get('city', '')
          try:
              order=Orders.objects.filter(order_id=orderid,city=city)
              if len(order)>0:
                   update=Orderupdate.objects.filter(order_id=orderid)
                   print(update)
                   allupdates=[]
                   for item in update:
                        allupdates.append({'text':item.update_desc , 'time':item.timestamp})
                        


                   response = json.dumps([allupdates,order[0].json_items], default=str)

                   return HttpResponse(response)
              else:
                   return HttpResponse('error')
          except Exception as e:
               return HttpResponse('error')




     return render(request,'shop/tracker.html')

def products(request,myid):
     product=Product.objects.filter(id=myid)
     print(product)
     return render(request,'shop/products.html',{'product':product[0]})

def checkout(request):
     if request.method=="POST":
          json_item=request.POST.get('itemsjson','')
          Name=request.POST.get('name','')
          addr=request.POST.get('Address','')
          city=request.POST.get('City','')
          state=request.POST.get('state','')
          zipcode=request.POST.get('zipcode','')


          order=Orders(json_items=json_item ,name=Name,address=addr,city=city,state=state,zipcode=zipcode)
          
          order.save()
          update=Orderupdate(order_id=order.order_id,update_desc="The order has been placed")
          update.save()
          thank = True
          id = order.order_id
          return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
     else:
          return render(request, 'shop/checkout.html')
          




# Create your views here.
