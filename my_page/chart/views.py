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


    # Position #1
    top_offer1 = Offers.objects.filter(published_at__gte=month_ago) \
                    .values('title') \
                    .annotate(title_count=Count('title')) \
                    .order_by('-title_count')[0:1]
    id_top_offer1 = Offers.objects.filter(title=top_offer1[0]['title']) \
        .values('id')
    most_popular_skill1 = Skills.objects.filter(id__in=id_top_offer1) \
                             .values('name') \
                             .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                             .order_by('-skill_count')[:10]
    top_offer1 = top_offer1[0]['title']

    # Position #2
    top_offer2 = Offers.objects.filter(published_at__gte=month_ago) \
                    .values('title') \
                    .annotate(title_count=Count('title')) \
                    .order_by('-title_count')[1:2]
    id_top_offer2 = Offers.objects.filter(title=top_offer2[0]['title']) \
        .values('id')
    most_popular_skill2 = Skills.objects.filter(id__in=id_top_offer2) \
                             .values('name') \
                             .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                             .order_by('-skill_count')[:10]
    top_offer2 = top_offer2[0]['title']

    # Position #3
    top_offer3 = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[2:3]
    id_top_offer3 = Offers.objects.filter(title=top_offer3[0]['title']) \
        .values('id')
    most_popular_skill3 = Skills.objects.filter(id__in=id_top_offer3) \
                              .values('name') \
                              .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                              .order_by('-skill_count')[:10]
    top_offer3 = top_offer3[0]['title']

    # Position #4
    top_offer4 = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[3:4]
    id_top_offer4 = Offers.objects.filter(title=top_offer4[0]['title']) \
        .values('id')
    most_popular_skill4 = Skills.objects.filter(id__in=id_top_offer4) \
                              .values('name') \
                              .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                              .order_by('-skill_count')[:10]
    top_offer4 = top_offer4[0]['title']

    # Position #5
    top_offer5 = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[4:5]
    id_top_offer5 = Offers.objects.filter(title=top_offer5[0]['title']) \
        .values('id')
    most_popular_skill5 = Skills.objects.filter(id__in=id_top_offer5) \
                              .values('name') \
                              .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                              .order_by('-skill_count')[:10]
    top_offer5 = top_offer5[0]['title']

    # Position #6
    top_offer6 = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[5:6]
    id_top_offer6 = Offers.objects.filter(title=top_offer6[0]['title']) \
        .values('id')
    most_popular_skill6 = Skills.objects.filter(id__in=id_top_offer6) \
                              .values('name') \
                              .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                              .order_by('-skill_count')[:10]
    top_offer6 = top_offer6[0]['title']

    # Position #7
    top_offer7 = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[6:7]
    id_top_offer7 = Offers.objects.filter(title=top_offer7[0]['title']) \
        .values('id')
    most_popular_skill7 = Skills.objects.filter(id__in=id_top_offer7) \
                              .values('name') \
                              .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                              .order_by('-skill_count')[:10]
    top_offer7 = top_offer7[0]['title']



    context = {
        'top_offers': top_offers,
        'top_skills': top_skills,
        'top_city': top_city,
        'city_to_work_on_site': city_to_work_on_site,
        'positions_on_day': positions_on_day,
        'positions_for_experience': positions_for_experience,
        'specializations': specializations,
        'top_offer1': top_offer1,
        'most_popular_skill1': most_popular_skill1,
        'top_offer2': top_offer2,
        'most_popular_skill2': most_popular_skill2,
        'top_offer3': top_offer3,
        'most_popular_skill3': most_popular_skill3,
        'top_offer4': top_offer4,
        'most_popular_skill4': most_popular_skill4,
        'top_offer5': top_offer5,
        'most_popular_skill5': most_popular_skill5,
        'top_offer6': top_offer6,
        'most_popular_skill6': most_popular_skill6,
        'top_offer7': top_offer7,
        'most_popular_skill7': most_popular_skill7,
    }
    return render(request, 'chart/main.html', context)



