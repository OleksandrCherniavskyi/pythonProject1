from django.http import HttpResponse
from django.template import loader
from .models import Offers, Skills
from django.shortcuts import render
from django.db.models import Count, Avg
from django.utils.timezone import now
import datetime


seven_days_ago = now() - datetime.timedelta(days=7)
month_ago = now() - datetime.timedelta(days=7)

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
                           .order_by('published_at')[:10]

    positions_for_experience = Offers.objects.filter(published_at__gte=month_ago)\
        .values('experience_level')\
        .annotate(experience_count=Count('experience_level'))\
        .order_by('experience_level')

    specializations = Offers.objects.filter(published_at__gte=month_ago)\
        .values("marker_icon")\
        .annotate(marker_count=Count('marker_icon'))\
        .order_by('-marker_count')[:7]



    context = {
        'top_offers': top_offers,
        'top_skills': top_skills,
        'top_city': top_city,
        'city_to_work_on_site': city_to_work_on_site,
        'positions_on_day': positions_on_day,
        'positions_for_experience': positions_for_experience,
        'specializations': specializations,
    }
    return render(request, 'chart/main.html', context)



def find_most_popular_skill(request):
    # Find the most popular 'title' in Offers
    top_offers = Offers.objects.filter(published_at__gte=month_ago) \
        .values('title') \
        .annotate(title_count=Count('title')) \
        .order_by('-title_count')\
        .first()
    if top_offers:
        most_popular_skill = Skills.objects.filter(offers__title=top_offers)\
            .values('name') \
                                 .annotate(skill_count=Count('name'), avg_level=Avg('level'))\
                                 .order_by('-skill_count')[:7]


        context = {
            'most_popular_skill': most_popular_skill,
        }


        return render(request, 'chart/find_most_popular_skill.html', context)
#def top_offers(request):
#
#    top_offers = Offers.objects.filter(published_at__gte=seven_days_ago) \
#                              .values('title') \
#                              .annotate(title_count=Count('title')) \
#                              .order_by('-title_count')[:7]
#    context = {
#        'top_offers': top_offers,
#    }
#    return render(request, 'chart/top_offers.html', context)
#
#
#
#
#def top_skills(request):
#    top_skills = Skills.objects.values('name') \
#        .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
#        .order_by('-skill_count')[:10]
#
#    template = loader.get_template('chart/top_skills.html')
#    context = {'top_skills': top_skills}
#    return HttpResponse(template.render(context, request))
#
#
#def top_city(request):
#
#    top_city = Offers.objects.filter(published_at__gte=seven_days_ago) \
#                              .values('city') \
#                              .annotate(city_count=Count('city')) \
#                              .order_by('-city_count')[:7]
#    context = {
#        'top_city': top_city,
#    }
#    return render(request, 'chart/top_city.html', context)
#
#def city_to_work_on_site(request):
#
#    city_to_work_on_site = Offers.objects.filter(published_at__gte=seven_days_ago,
#                                       workplace_type__in=['partly_remote', 'office']) \
#                              .values('city') \
#                              .annotate(city_count=Count('city')) \
#                              .order_by('-city_count')[:7]
#    context = {
#        'city_to_work_on_site': city_to_work_on_site,
#    }
#    return render(request, 'chart/city_to_work_on_site.html', context)