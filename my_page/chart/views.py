from django.http import HttpResponse
from django.template import loader
from .models import Offers, Skills
from django.shortcuts import render
from django.db.models import Count, Avg
from django.utils.timezone import now
import datetime


seven_days_ago = now() - datetime.timedelta(days=7)
month_ago = now() - datetime.timedelta(days=30)

def main(request):

    top_offers = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[:7]

    top_skills = Skills.objects.values('name') \
                     .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                     .order_by('-skill_count')[:7]

    top_city = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('city') \
                     .annotate(city_count=Count('city')) \
                     .order_by('-city_count')[:7]

    city_to_work_on_site = Offers.objects.filter(published_at__gte=month_ago,
                                                 workplace_type__in=['partly_remote', 'office']) \
                               .values('city') \
                               .annotate(city_count=Count('city')) \
                               .order_by('-city_count')[:7]

    positions_on_day = Offers.objects.exclude(published_at="2023-05-23") \
                           .values('published_at') \
                           .annotate(title_count=Count('title')) \
                           .order_by('published_at')

    positions_for_experience = Offers.objects.filter(published_at__gte=month_ago)\
        .values('experience_level')\
        .annotate(experience_count=Count('experience_level'))\
        .order_by('experience_level')

    specializations = Offers.objects.filter(published_at__gte=month_ago)\
        .values("marker_icon")\
        .annotate(marker_count=Count('marker_icon'))\
        .order_by('-marker_count')[:7]


    top_offer = Offers.objects.filter(published_at__gte=month_ago) \
                    .values('title') \
                    .annotate(title_count=Count('title')) \
                    .order_by('-title_count')[0:1]
    id_top_offer = Offers.objects.filter(title=top_offer[0]['title']) \
        .values('id')
    most_popular_skill = Skills.objects.filter(id__in=id_top_offer) \
                             .values('name') \
                             .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                             .order_by('-skill_count')[:10]
    top_offer = top_offer[0]['title']




    context = {
        'top_offers': top_offers,
        'top_skills': top_skills,
        'top_city': top_city,
        'city_to_work_on_site': city_to_work_on_site,
        'positions_on_day': positions_on_day,
        'positions_for_experience': positions_for_experience,
        'specializations': specializations,
        'top_offer': top_offer,
        'most_popular_skill': most_popular_skill,
    }
    return render(request, 'chart/main.html', context)



#def find_most_popular_skill(request):
#
#    top_offer = Offers.objects.filter(published_at__gte=month_ago) \
#        .values('title') \
#        .annotate(title_count=Count('title')) \
#        .order_by('-title_count')[1:2]
#
#    id_top_offer = Offers.objects.filter(title=top_offer[0]['title'])\
#        .values('id')
#
#    most_popular_skill = Skills.objects.filter(id__in=id_top_offer) \
#        .values('name') \
#        .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
#        .order_by('-skill_count')[:10]
#    top_offer = top_offer[0]['title']
#
#    context = {
#        'top_offer': top_offer,
#        'most_popular_skill': most_popular_skill,
#    }
#    return render(request, 'chart/main.html', context)
