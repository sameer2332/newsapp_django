from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['alldata'] = inshort_data
    return render(request, 'newsapp\home.html', records)

def business(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=business"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['businessdata'] = inshort_data
    return render(request, 'newsapp/business.html', records)


    
def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['sportsdata'] = inshort_data
    return render(request, 'newsapp\sports.html', records)

def science(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=science"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['sciencedata'] = inshort_data
    return render(request, 'newsapp\science.html', records)

def entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['entertainmentdata'] = inshort_data
    return render(request, 'newsapp\entertainment.html', records)


   