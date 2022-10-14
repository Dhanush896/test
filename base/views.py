from django.shortcuts import render
from base.models import crudst
from django.contrib import messages

def stdisplay(request):
    results=crudst.objects.all()
    return render(request,"base.html",{"crudst":results})

def stinsert(request):
    if request.method == "POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('sno'):
            savest = crudst()
            savest.stname=request.POST.get('stname')
            savest.stemail=request.POST.get('stemail')
            savest.staddress=request.POST.get('staddress')
            savest.sno=request.POST.get('sno')
            savest.save()
            messages.success(request,"the record"+savest.stname+"is saved successfully..!")
            return render(request,"create.html")
    else:
        return render(request,"create.html")

