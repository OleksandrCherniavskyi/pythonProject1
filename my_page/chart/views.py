from django.http import HttpResponse
from django.template import loader
from .models import Offers
from django.shortcuts import render


def top_7(request):
    all_offers = Offers.objects.all()
    template = loader.get_template("tem.html")
    context = {
        "myoffers": all_offers,
    }
    return HttpResponse(template.render(context, request))


