from django.shortcuts import render,redirect
from invent.models import productmovement as pm
from invent.models import product
from invent.models import location

def home(request):
    return render (request, 'index.html')

def viewpro(request):
    pro = product.objects.all()
    return render(request, 'viewproduct.html', {'pro' : pro})

def addpro(request):
    if request.method=="POST":
        proid = request.POST['pid']
        data = product.objects.create(product_id=proid)
        data.save
    return render(request, 'addproduct.html')
    
def editpro(request,pdid):
    idno = product.objects.get(id=pdid)
    if request.method=="POST":
        proid = request.POST['pid']
        idno.product_id=proid
        idno.save()
        return redirect('viewproduct')    
    return render (request, 'editproduct.html', {'idno':idno})
    
    
def viewloc(request):
    loc = location.objects.all()
    return render(request, 'viewlocation.html', {'loc' : loc})

def addloc(request):
    if request.method=="POST":
        locid = request.POST['lid']
        data=location.objects.create(location_id=locid)
        data.save
    return render (request, 'addlocation.html')

def editloc(request, ltid):
    lcid=location.objects.get(id=ltid)
    if request.method=='POST':
        locid = request.POST['lid']
        lcid.location_id=locid
        lcid.save()
        return redirect ('viewlocation')    
    return render (request, 'editlocation.html',{'locid':lcid})
    
    
def viewmvmnt(request):
    mv = pm.objects.all()
    return render(request, 'viewmovement.html', {'mv': mv})

def addmvmnt(request):
    if request.method=="POST":
        mvid = request.POST['mid']
        floc = request.POST['floc']
        tloc = request.POST['tloc']
        qty =  request.POST['qty']
        data = pm.objects.create(movement_id=mvid, from_location=floc, to_location=tloc, qyt=qty)
        data.save()
    return render (request, 'addmovement.html')

def editmvmnt(request):
    return render (request, 'editmovement.html')    
    
    
