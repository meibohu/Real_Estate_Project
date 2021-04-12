from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):    ## Home page
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]   ##前三个
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'pages/index.html', context)

def about(request):     ## About page
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    ## MVP check: get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,        ## 前端要用key
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)