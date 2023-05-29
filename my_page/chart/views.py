from django.http import HttpResponse
from django.template import loader
from .models import Offers, Skills
from django.shortcuts import render
from django.db.models import Count, Avg
from django.utils.timezone import now
import datetime


#def main(request):
#    return render(request, 'chart/main.html')



def main(request):
    seven_days_ago = now() - datetime.timedelta(days=7)
    top_offers = Offers.objects.filter(published_at__gte=seven_days_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[:7]

    top_skills = Skills.objects.values('name') \
                     .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                     .order_by('-skill_count')[:10]

    context = {
        'top_offers': top_offers,
        'top_skills': top_skills,
    }
    return render(request, 'chart/main.html', context)


def top_offers(request):
    seven_days_ago = now() - datetime.timedelta(days=7)
    top_offers = Offers.objects.filter(published_at__gte=seven_days_ago) \
                              .values('title') \
                              .annotate(title_count=Count('title')) \
                              .order_by('-title_count')[:7]
    context = {
        'top_offers': top_offers,
    }
    return render(request, 'chart/top_offers.html', context)




def top_skills(request):
    top_skills = Skills.objects.values('name') \
        .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
        .order_by('-skill_count')[:10]

    template = loader.get_template('chart/top_skills.html')
    context = {'top_skills': top_skills}
    return HttpResponse(template.render(context, request))
