from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing

# Create your views here.

# listings
def index(request):
    # listings = Listing.objects.all()  
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)    #if is_published = false 去掉
    paginator = Paginator(listings, 3) 
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        # 'listings': listings 
        'listings': paged_listings        
    }
    return render(request, 'listings/listings.html', context)   # pass value in

# listing
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)    # check to see if it exists

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)
    
# search
def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:   # not empty
            queryset_list = queryset_list.filter(description__icontains=keywords)   ## case insensitive

    ## City 
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city) 

    ## State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    ## Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)     ## less and equal than
 
    ## Price
    if 'price' in request.GET:
        price = request.GET['price']     ## is the name of price in html
        if price:
            queryset_list = queryset_list.filter(price__lte=price)     ## less and equal than

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
