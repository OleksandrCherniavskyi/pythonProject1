from django.http import HttpResponse
from django.template import loader
from .models import Offers, Skills, BrandsOffice
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

    # Specialisation #1
    specialisation1 = Offers.objects.filter(published_at__gte=month_ago) \
                          .values('marker_icon') \
                          .annotate(marker_icon_count=Count('marker_icon')) \
                          .order_by('-marker_icon_count')[0:1]
    id_specialisation1 = Offers.objects.filter(marker_icon=specialisation1[0]['marker_icon']) \
        .values('id')
    specialisation_skill1 = Skills.objects.filter(id__in=id_specialisation1) \
                                .values('name') \
                                .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                                .order_by('-skill_count')[:10]
    specialisation1 = specialisation1[0]['marker_icon']

    # Specialisation #2
    specialisation2 = Offers.objects.filter(published_at__gte=month_ago) \
                          .values('marker_icon') \
                          .annotate(marker_icon_count=Count('marker_icon')) \
                          .order_by('-marker_icon_count')[1:2]
    id_specialisation2 = Offers.objects.filter(marker_icon=specialisation2[0]['marker_icon']) \
        .values('id')
    specialisation_skill2 = Skills.objects.filter(id__in=id_specialisation2) \
                                .values('name') \
                                .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                                .order_by('-skill_count')[:10]
    specialisation2 = specialisation2[0]['marker_icon']

    # Specialisation #3
    specialisation3 = Offers.objects.filter(published_at__gte=month_ago) \
                          .values('marker_icon') \
                          .annotate(marker_icon_count=Count('marker_icon')) \
                          .order_by('-marker_icon_count')[2:3]
    id_specialisation3 = Offers.objects.filter(marker_icon=specialisation3[0]['marker_icon']) \
        .values('id')
    specialisation_skill3 = Skills.objects.filter(id__in=id_specialisation3) \
                                .values('name') \
                                .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                                .order_by('-skill_count')[:10]
    specialisation3 = specialisation3[0]['marker_icon']

    # Specialisation #4
    specialisation4 = Offers.objects.filter(published_at__gte=month_ago) \
                          .values('marker_icon') \
                          .annotate(marker_icon_count=Count('marker_icon')) \
                          .order_by('-marker_icon_count')[3:4]
    id_specialisation4 = Offers.objects.filter(marker_icon=specialisation4[0]['marker_icon']) \
        .values('id')
    specialisation_skill4 = Skills.objects.filter(id__in=id_specialisation4) \
                                .values('name') \
                                .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                                .order_by('-skill_count')[:10]
    specialisation4 = specialisation4[0]['marker_icon']

    # Specialisation #5
    specialisation5 = Offers.objects.filter(published_at__gte=month_ago) \
                          .values('marker_icon') \
                          .annotate(marker_icon_count=Count('marker_icon')) \
                          .order_by('-marker_icon_count')[4:5]
    id_specialisation5 = Offers.objects.filter(marker_icon=specialisation5[0]['marker_icon']) \
        .values('id')
    specialisation_skill5 = Skills.objects.filter(id__in=id_specialisation5) \
                                .values('name') \
                                .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                                .order_by('-skill_count')[:10]
    specialisation5 = specialisation5[0]['marker_icon']

    # Specialisation #6
    specialisation6 = Offers.objects.filter(published_at__gte=month_ago) \
                          .values('marker_icon') \
                          .annotate(marker_icon_count=Count('marker_icon')) \
                          .order_by('-marker_icon_count')[5:6]
    id_specialisation6 = Offers.objects.filter(marker_icon=specialisation6[0]['marker_icon']) \
        .values('id')
    specialisation_skill6 = Skills.objects.filter(id__in=id_specialisation6) \
                                .values('name') \
                                .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                                .order_by('-skill_count')[:10]
    specialisation6 = specialisation6[0]['marker_icon']

    # Specialisation #7
    specialisation7 = Offers.objects.filter(published_at__gte=month_ago) \
                          .values('marker_icon') \
                          .annotate(marker_icon_count=Count('marker_icon')) \
                          .order_by('-marker_icon_count')[6:7]
    id_specialisation7 = Offers.objects.filter(marker_icon=specialisation7[0]['marker_icon']) \
        .values('id')
    specialisation_skill7 = Skills.objects.filter(id__in=id_specialisation7) \
                                .values('name') \
                                .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                                .order_by('-skill_count')[:10]
    specialisation7 = specialisation7[0]['marker_icon']

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
        'specialisation_skill1': specialisation_skill1,
        'specialisation1': specialisation1,
        'specialisation_skill2': specialisation_skill2,
        'specialisation2': specialisation2,
        'specialisation_skill3': specialisation_skill3,
        'specialisation3': specialisation3,
        'specialisation_skill4': specialisation_skill4,
        'specialisation4': specialisation4,
        'specialisation_skill5': specialisation_skill5,
        'specialisation5': specialisation5,
        'specialisation_skill6': specialisation_skill6,
        'specialisation6': specialisation6,
        'specialisation_skill7': specialisation_skill7,
        'specialisation7': specialisation7,
    }
    return render(request, 'chart/main.html', context)


def work_type(request):
    experience_level = Offers.objects.values('experience_level').annotate(count=Count('experience_level'))
    work_type_office = Offers.objects.filter(published_at__gte=month_ago, workplace_type='office') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))

    work_type_hybrid = Offers.objects.filter(published_at__gte=month_ago, workplace_type='partly_remote') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))

    work_type_remote = Offers.objects.filter(published_at__gte=month_ago, workplace_type='remote') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))


    work_type_jr = Offers.objects.filter(published_at__gte=month_ago, experience_level__in=['junior'])\
        .values('workplace_type')\
        .annotate(count_workplace_type=Count('workplace_type'))\
        .order_by('workplace_type')

    work_type_mid = Offers.objects.filter(published_at__gte=month_ago, experience_level__in=['mid']) \
        .values('workplace_type') \
        .annotate(count_workplace_type=Count('workplace_type')) \
        .order_by('workplace_type')

    work_type_sr = Offers.objects.filter(published_at__gte=month_ago, experience_level__in=['senior']) \
        .values('workplace_type') \
        .annotate(count_workplace_type=Count('workplace_type')) \
        .order_by('workplace_type')

    total_count_jr = Offers.objects.filter(published_at__gte=month_ago, experience_level__in=['junior']).count()
    total_count_mid = Offers.objects.filter(published_at__gte=month_ago, experience_level__in=['mid']).count()
    total_count_sr = Offers.objects.filter(published_at__gte=month_ago, experience_level__in=['senior']).count()
    # Calculate percentages
    for work_type in work_type_jr:
        work_type['percentage'] = work_type['count_workplace_type'] * 100.0 / total_count_jr

    for work_type in work_type_mid:
        work_type['percentage'] = work_type['count_workplace_type'] * 100.0 / total_count_mid

    for work_type in work_type_sr:
        work_type['percentage'] = work_type['count_workplace_type'] * 100.0 / total_count_sr

    context = {
        'work_type_jr': work_type_jr,
        'work_type_mid': work_type_mid,
        'work_type_sr': work_type_sr,
        'total_count_jr': total_count_jr,
        'total_count_mid': total_count_mid,
        'total_count_sr': total_count_sr,
        'experience_level': experience_level,
        'work_type_office': work_type_office,
        'work_type_hybrid': work_type_hybrid,
        'work_type_remote': work_type_remote,
    }
    return render(request, 'chart/work_type.html', context)