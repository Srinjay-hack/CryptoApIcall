import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    apidata=requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    
    return render(request,"index.html",{"apidata":apidata})