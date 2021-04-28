import itertools

from django.shortcuts import render, redirect

from eshop_products.models import Product
from eshop_sliders.models import Silders
from eshop_settings.models import SiteSettings
from eshop_account.forms import NewsBulletin


# header code behind

def header(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    context = {
        "setting": site_settings
    }

    return render(request, 'shared/header.html', context)


def footer(request, *args, **kwargs):
    site_settings = SiteSettings.objects.first()
    context = {
        "setting": site_settings,
        "news": NewsBulletin
    }
    return render(request, "shared/footer.html", context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders = Silders.objects.all()
    most_visit_product = Product.objects.order_by('-visit_count').all()[:8]
    latest_products = Product.objects.order_by('-id').all()[:8]
    context = {
        "data": "new data",
        'sliders': sliders,
        "most_visit": my_grouper(4, most_visit_product),
        "latest_products":my_grouper(4, latest_products)

    }
    return render(request, "Home_page.html", context)


def about_page(request):
    site_settings = SiteSettings.objects.first()
    context = {
        "setting": site_settings
    }
    return render(request, 'about_page.html', context)
