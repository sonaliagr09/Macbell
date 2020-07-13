from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import category
# Create your views here.
def categories(request):
    if request.method =='POST':
        company_name=request.POST['company_name']
        company_email=request.POST['company_email']
        website=request.POST['website']
        company_address=request.POST['company_address']
        city=request.POST['city']
        industry=request.POST['industry']
        business=request.POST['business']
        company=request.POST['company']
        temp=category(company_name=company_name,company_email=company_email,website=website,company_address=company_address,
        city=city,industry=industry,business=business,company=company)
        temp.save()
        return redirect('/')
    else:
        return render(request,'categories.html')
