from django.db.models.functions import ExtractWeek, ExtractMonth

from .models import Offers, Skills, BrandsOffice, EmploymentTypes, Brands
from django.shortcuts import render
from django.db.models import Count, Avg
from django.utils.timezone import now
import datetime


seven_days_ago = now() - datetime.timedelta(days=7)
month_ago = now() - datetime.timedelta(days=30)
quartal_ago = now() - datetime.timedelta(days=90)


def week(request):

    top_offers = Offers.objects.filter(published_at__gte=seven_days_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[:7]

    offers = Offers.objects.filter(published_at__gte=seven_days_ago) \
                     .values('id')
    junior_offers = Offers.objects.filter(published_at__gte=seven_days_ago, experience_level='junior') \
        .values('id')

    mid_offers = Offers.objects.filter(published_at__gte=seven_days_ago, experience_level='mid') \
        .values('id')

    senior_offers = Offers.objects.filter(published_at__gte=seven_days_ago, experience_level='senior') \
        .values('id')


    top_skills = Skills.objects.filter(id__in=offers).values('name') \
                     .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                     .order_by('-skill_count')[:10]

    top_city = Offers.objects.filter(published_at__gte=seven_days_ago) \
                     .values('city') \
                     .annotate(city_count=Count('city')) \
                     .order_by('-city_count')[:7]

    city_to_work_on_site = Offers.objects.filter(published_at__gte=seven_days_ago,
                                                 workplace_type__in=['partly_remote', 'office']) \
                               .values('city') \
                               .annotate(city_count=Count('city')) \
                               .order_by('-city_count')[:7]

    positions_on_day = Offers.objects.exclude(published_at__lt="2023-06-18") \
        .values('published_at') \
        .annotate(title_count=Count('title')) \
        .order_by('published_at')

    positions_for_experience = Offers.objects.filter(published_at__gte=seven_days_ago)\
        .values('experience_level')\
        .annotate(experience_count=Count('experience_level'))\
        .order_by('experience_level')

    specializations = Offers.objects.filter(published_at__gte=seven_days_ago)\
        .values("marker_icon")\
        .annotate(marker_count=Count('marker_icon'))\
        .order_by('-marker_count')[:7]


    # Position #1
    top_offer1 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    top_offer2 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    top_offer3 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    top_offer4 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    top_offer5 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    top_offer6 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    top_offer7 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    specialisation1 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    specialisation2 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    specialisation3 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    specialisation4 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    specialisation5 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    specialisation6 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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
    specialisation7 = Offers.objects.filter(published_at__gte=seven_days_ago) \
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

    experience_level = Offers.objects.values('experience_level').annotate(count=Count('experience_level'))
    work_type_office = Offers.objects.filter(published_at__gte=seven_days_ago, workplace_type='office') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))

    work_type_hybrid = Offers.objects.filter(published_at__gte=seven_days_ago, workplace_type='partly_remote') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))

    work_type_remote = Offers.objects.filter(published_at__gte=seven_days_ago, workplace_type='remote') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))

    junior_positions = Offers.objects.filter(published_at__gte=seven_days_ago, experience_level='junior') \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[:7]

    mid_positions = Offers.objects.filter(published_at__gte=seven_days_ago, experience_level='mid') \
                           .values('title') \
                           .annotate(title_count=Count('title')) \
                           .order_by('-title_count')[:7]

    senior_positions = Offers.objects.filter(published_at__gte=seven_days_ago, experience_level='senior') \
                        .values('title') \
                        .annotate(title_count=Count('title')) \
                        .order_by('-title_count')[:7]

    min_avg1 = EmploymentTypes.objects.filter(id__in=id_top_offer1, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg1 = EmploymentTypes.objects.filter(id__in=id_top_offer1, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg2 = EmploymentTypes.objects.filter(id__in=id_top_offer2, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg2 = EmploymentTypes.objects.filter(id__in=id_top_offer2, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg3 = EmploymentTypes.objects.filter(id__in=id_top_offer3, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg3 = EmploymentTypes.objects.filter(id__in=id_top_offer3, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg4 = EmploymentTypes.objects.filter(id__in=id_top_offer4, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg4 = EmploymentTypes.objects.filter(id__in=id_top_offer4, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg5 = EmploymentTypes.objects.filter(id__in=id_top_offer5, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg5 = EmploymentTypes.objects.filter(id__in=id_top_offer5, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg6 = EmploymentTypes.objects.filter(id__in=id_top_offer6, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg6 = EmploymentTypes.objects.filter(id__in=id_top_offer6, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg7 = EmploymentTypes.objects.filter(id__in=id_top_offer7, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg7 = EmploymentTypes.objects.filter(id__in=id_top_offer7, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    week = Offers.objects.exclude(published_at__lt="2023-06-19") \
        .values('published_at') \
        .annotate(week_number=ExtractWeek('published_at')).order_by() \
        .annotate(title_count=Count('title'))

    day_counts = {'Mon': [0, 0], 'Tue': [0, 0], 'Wed': [0, 0], 'Thu': [0, 0], 'Fri': [0, 0], 'Sat': [0, 0],
                  'Sun': [0, 0]}
    for item in week:
        day = item['published_at'].strftime("%a")  # Get the day of the week (e.g., 'Mon', 'Tue', etc.)
        count = item['title_count']
        day_counts[day][0] += count
        day_counts[day][1] += 1

    averages = {}
    for day, count_data in day_counts.items():
        total_count = count_data[0]
        occurrence = count_data[1]
        average = total_count / occurrence if occurrence > 0 else 0
        averages[day] = average

    positions_per_week = week.values('week_number').annotate(title_count=Count('title'))

    j_positions_for_company = Offers.objects.filter(experience_level='junior', published_at__gte=seven_days_ago) \
                     .values('company_name') \
                     .annotate(count_offers=Count('company_name')) \
                     .order_by('-count_offers')[:7]

    m_positions_for_company = Offers.objects.filter(experience_level='mid', published_at__gte=seven_days_ago) \
        .values('company_name') \
        .annotate(count_offers=Count('company_name')) \
        .order_by('-count_offers')[:7]

    s_positions_for_company = Offers.objects.filter(experience_level='senior', published_at__gte=seven_days_ago) \
        .values('company_name') \
        .annotate(count_offers=Count('company_name')) \
        .order_by('-count_offers')[:7]

    j_employment_type_counts = EmploymentTypes.objects.filter( id__in=junior_offers ) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('type')

    m_employment_type_counts = EmploymentTypes.objects.filter(id__in=mid_offers) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('type')

    s_employment_type_counts = EmploymentTypes.objects.filter( id__in=senior_offers ) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('type')


    context = {
        'j_employment_type_counts': j_employment_type_counts,
        'm_employment_type_counts': m_employment_type_counts,
        's_employment_type_counts': s_employment_type_counts,
        'j_positions_for_company': j_positions_for_company,
        'm_positions_for_company': m_positions_for_company,
        's_positions_for_company': s_positions_for_company,
        'positions_per_week': positions_per_week,
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
        'experience_level': experience_level,
        'work_type_office': work_type_office,
        'work_type_hybrid': work_type_hybrid,
        'work_type_remote': work_type_remote,
        'junior_positions': junior_positions,
        'mid_positions': mid_positions,
        'senior_positions': senior_positions,
        'min_avg1': min_avg1,
        'max_avg1': max_avg1,
        'min_avg2': min_avg2,
        'max_avg2': max_avg2,
        'min_avg3': min_avg3,
        'max_avg3': max_avg3,
        'min_avg4': min_avg4,
        'max_avg4': max_avg4,
        'min_avg5': min_avg5,
        'max_avg5': max_avg5,
        'min_avg6': min_avg6,
        'max_avg6': max_avg6,
        'min_avg7': min_avg7,
        'max_avg7': max_avg7,
        'week': week,
        'averages': averages
    }
    return render(request, 'chart/week.html', context)



def month(request):

    top_offers = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[:7]

    offers = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('id')

    junior_offers = Offers.objects.filter(published_at__gte=month_ago, experience_level='junior') \
        .values('id')

    mid_offers = Offers.objects.filter(published_at__gte=month_ago, experience_level='mid') \
        .values('id')

    senior_offers = Offers.objects.filter(published_at__gte=month_ago, experience_level='senior') \
        .values('id')

    top_skills = Skills.objects.filter(id__in=offers).values('name') \
                     .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                     .order_by('-skill_count')[:10]

    top_city = Offers.objects.filter(published_at__gte=month_ago) \
                     .values('city') \
                     .annotate(city_count=Count('city')) \
                     .order_by('-city_count')[:7]

    city_to_work_on_site = Offers.objects.filter(published_at__gte=month_ago,
                                                 workplace_type__in=['partly_remote', 'office']) \
                               .values('city') \
                               .annotate(city_count=Count('city')) \
                               .order_by('-city_count')[:7]

    positions_on_day = Offers.objects.exclude(published_at__lt="2023-06-18") \
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

    junior_positions = Offers.objects.filter(published_at__gte=month_ago, experience_level='junior') \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[:7]

    mid_positions = Offers.objects.filter(published_at__gte=month_ago, experience_level='mid') \
                           .values('title') \
                           .annotate(title_count=Count('title')) \
                           .order_by('-title_count')[:7]

    senior_positions = Offers.objects.filter(published_at__gte=month_ago, experience_level='senior') \
                        .values('title') \
                        .annotate(title_count=Count('title')) \
                        .order_by('-title_count')[:7]

    min_avg1 = EmploymentTypes.objects.filter(id__in=id_top_offer1, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg1 = EmploymentTypes.objects.filter(id__in=id_top_offer1, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg2 = EmploymentTypes.objects.filter(id__in=id_top_offer2, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg2 = EmploymentTypes.objects.filter(id__in=id_top_offer2, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg3 = EmploymentTypes.objects.filter(id__in=id_top_offer3, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg3 = EmploymentTypes.objects.filter(id__in=id_top_offer3, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg4 = EmploymentTypes.objects.filter(id__in=id_top_offer4, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg4 = EmploymentTypes.objects.filter(id__in=id_top_offer4, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg5 = EmploymentTypes.objects.filter(id__in=id_top_offer5, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg5 = EmploymentTypes.objects.filter(id__in=id_top_offer5, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg6 = EmploymentTypes.objects.filter(id__in=id_top_offer6, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg6 = EmploymentTypes.objects.filter(id__in=id_top_offer6, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg7 = EmploymentTypes.objects.filter(id__in=id_top_offer7, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg7 = EmploymentTypes.objects.filter(id__in=id_top_offer7, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    week = Offers.objects.exclude(published_at__lt="2023-06-19") \
        .values('published_at') \
        .annotate(week_number=ExtractWeek('published_at')).order_by() \
        .annotate(title_count=Count('title'))

    day_counts = {'Mon': [0, 0], 'Tue': [0, 0], 'Wed': [0, 0], 'Thu': [0, 0], 'Fri': [0, 0], 'Sat': [0, 0],
                  'Sun': [0, 0]}
    for item in week:
        day = item['published_at'].strftime("%a")  # Get the day of the week (e.g., 'Mon', 'Tue', etc.)
        count = item['title_count']
        day_counts[day][0] += count
        day_counts[day][1] += 1

    averages = {}
    for day, count_data in day_counts.items():
        total_count = count_data[0]
        occurrence = count_data[1]
        average = total_count / occurrence if occurrence > 0 else 0
        averages[day] = average

    positions_per_week = week.values('week_number').annotate(title_count=Count('title')).order_by('week_number')

    junior_positions_week = positions_per_week.filter(experience_level='junior')

    mid_positions_week = positions_per_week.filter(experience_level='mid')

    senior_positions_week = positions_per_week.filter(experience_level='senior')

    j_positions_for_company = Offers.objects.filter(experience_level='junior', published_at__gte=month_ago) \
                                  .values('company_name') \
                                  .annotate(count_offers=Count('company_name')) \
                                  .order_by('-count_offers')[:7]

    m_positions_for_company = Offers.objects.filter(experience_level='mid', published_at__gte=month_ago) \
                                  .values('company_name') \
                                  .annotate(count_offers=Count('company_name')) \
                                  .order_by('-count_offers')[:7]

    s_positions_for_company = Offers.objects.filter(experience_level='senior', published_at__gte=month_ago) \
                                  .values('company_name') \
                                  .annotate(count_offers=Count('company_name')) \
                                  .order_by('-count_offers')[:7]

    j_employment_type_counts = EmploymentTypes.objects.filter(id__in=junior_offers) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('type')

    m_employment_type_counts = EmploymentTypes.objects.filter(id__in=mid_offers) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('type')

    s_employment_type_counts = EmploymentTypes.objects.filter(id__in=senior_offers) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('-type')

    context = {
        'j_employment_type_counts': j_employment_type_counts,
        'm_employment_type_counts': m_employment_type_counts,
        's_employment_type_counts': s_employment_type_counts,
        'j_positions_for_company': j_positions_for_company,
        'm_positions_for_company': m_positions_for_company,
        's_positions_for_company': s_positions_for_company,
        'junior_positions_week': junior_positions_week,
        'mid_positions_week': mid_positions_week,
        'senior_positions_week': senior_positions_week,
        'positions_per_week': positions_per_week,
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
        'experience_level': experience_level,
        'work_type_office': work_type_office,
        'work_type_hybrid': work_type_hybrid,
        'work_type_remote': work_type_remote,
        'junior_positions': junior_positions,
        'mid_positions': mid_positions,
        'senior_positions': senior_positions,
        'min_avg1': min_avg1,
        'max_avg1': max_avg1,
        'min_avg2': min_avg2,
        'max_avg2': max_avg2,
        'min_avg3': min_avg3,
        'max_avg3': max_avg3,
        'min_avg4': min_avg4,
        'max_avg4': max_avg4,
        'min_avg5': min_avg5,
        'max_avg5': max_avg5,
        'min_avg6': min_avg6,
        'max_avg6': max_avg6,
        'min_avg7': min_avg7,
        'max_avg7': max_avg7,
        'week': week,
        'averages': averages
    }
    return render(request, 'chart/month.html', context)


def quartal(request):

    top_offers = Offers.objects.filter(published_at__gte=quartal_ago) \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[:7]

    offers = Offers.objects.filter(published_at__gte=quartal_ago) \
                     .values('id')

    junior_offers = Offers.objects.filter(published_at__gte=quartal_ago, experience_level='junior') \
        .values('id')

    mid_offers = Offers.objects.filter(published_at__gte=quartal_ago, experience_level='mid') \
        .values('id')

    senior_offers = Offers.objects.filter(published_at__gte=quartal_ago, experience_level='senior') \
        .values('id')

    top_skills = Skills.objects.filter(id__in=offers).values('name') \
                     .annotate(skill_count=Count('name'), avg_level=Avg('level')) \
                     .order_by('-skill_count')[:10]

    top_city = Offers.objects.filter(published_at__gte=quartal_ago) \
                     .values('city') \
                     .annotate(city_count=Count('city')) \
                     .order_by('-city_count')[:7]

    city_to_work_on_site = Offers.objects.filter(published_at__gte=quartal_ago,
                                                 workplace_type__in=['partly_remote', 'office']) \
                               .values('city') \
                               .annotate(city_count=Count('city')) \
                               .order_by('-city_count')[:7]

    positions_on_day = Offers.objects.exclude(published_at__lt="2023-06-18") \
        .values('published_at') \
        .annotate(title_count=Count('title')) \
        .order_by('published_at')

    positions_for_experience = Offers.objects.filter(published_at__gte=quartal_ago)\
        .values('experience_level')\
        .annotate(experience_count=Count('experience_level'))\
        .order_by('experience_level')

    specializations = Offers.objects.filter(published_at__gte=quartal_ago)\
        .values("marker_icon")\
        .annotate(marker_count=Count('marker_icon'))\
        .order_by('-marker_count')[:7]


    # Position #1
    top_offer1 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    top_offer2 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    top_offer3 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    top_offer4 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    top_offer5 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    top_offer6 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    top_offer7 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    specialisation1 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    specialisation2 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    specialisation3 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    specialisation4 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    specialisation5 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    specialisation6 = Offers.objects.filter(published_at__gte=quartal_ago) \
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
    specialisation7 = Offers.objects.filter(published_at__gte=quartal_ago) \
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

    experience_level = Offers.objects.values('experience_level').annotate(count=Count('experience_level'))

    work_type_office = Offers.objects.filter(published_at__gte=quartal_ago, workplace_type='office') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))

    work_type_hybrid = Offers.objects.filter(published_at__gte=quartal_ago, workplace_type='partly_remote') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))

    work_type_remote = Offers.objects.filter(published_at__gte=quartal_ago, workplace_type='remote') \
        .values('experience_level') \
        .annotate(count_workplace_type=Count('workplace_type'))

    junior_positions = Offers.objects.filter(published_at__gte=quartal_ago, experience_level='junior') \
                     .values('title') \
                     .annotate(title_count=Count('title')) \
                     .order_by('-title_count')[:7]

    mid_positions = Offers.objects.filter(published_at__gte=quartal_ago, experience_level='mid') \
                           .values('title') \
                           .annotate(title_count=Count('title')) \
                           .order_by('-title_count')[:7]

    senior_positions = Offers.objects.filter(published_at__gte=quartal_ago, experience_level='senior') \
                        .values('title') \
                        .annotate(title_count=Count('title')) \
                        .order_by('-title_count')[:7]

    min_avg1 = EmploymentTypes.objects.filter(id__in=id_top_offer1, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg1 = EmploymentTypes.objects.filter(id__in=id_top_offer1, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg2 = EmploymentTypes.objects.filter(id__in=id_top_offer2, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg2 = EmploymentTypes.objects.filter(id__in=id_top_offer2, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg3 = EmploymentTypes.objects.filter(id__in=id_top_offer3, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg3 = EmploymentTypes.objects.filter(id__in=id_top_offer3, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg4 = EmploymentTypes.objects.filter(id__in=id_top_offer4, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg4 = EmploymentTypes.objects.filter(id__in=id_top_offer4, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg5 = EmploymentTypes.objects.filter(id__in=id_top_offer5, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg5 = EmploymentTypes.objects.filter(id__in=id_top_offer5, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg6 = EmploymentTypes.objects.filter(id__in=id_top_offer6, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg6 = EmploymentTypes.objects.filter(id__in=id_top_offer6, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    min_avg7 = EmploymentTypes.objects.filter(id__in=id_top_offer7, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('from_salary')).order_by('-type_count')

    max_avg7 = EmploymentTypes.objects.filter(id__in=id_top_offer7, currency='pln') \
        .values('type').annotate(type_count=Count('type'), avg_level=Avg('to_salary')).order_by('-type_count')

    month = Offers.objects.exclude(published_at__lt="2023-07-01") \
        .values('published_at') \
        .annotate(month_number=ExtractMonth('published_at')).order_by() \
        .annotate(title_count=Count('title'))

    positions_per_month = month.values('month_number').annotate(title_count=Count('title')).order_by('month_number')

    junior_positions_month = positions_per_month.filter(experience_level='junior')


    mid_positions_month = positions_per_month.filter(experience_level='mid')


    senior_positions_month =  positions_per_month.filter(experience_level='senior')

    j_positions_for_company = Offers.objects.filter(experience_level='junior', published_at__gte=quartal_ago) \
                                  .values('company_name') \
                                  .annotate(count_offers=Count('company_name')) \
                                  .order_by('-count_offers')[:7]

    m_positions_for_company = Offers.objects.filter(experience_level='mid', published_at__gte=quartal_ago) \
                                  .values('company_name') \
                                  .annotate(count_offers=Count('company_name')) \
                                  .order_by('-count_offers')[:7]

    s_positions_for_company = Offers.objects.filter(experience_level='senior', published_at__gte=quartal_ago) \
                                  .values('company_name') \
                                  .annotate(count_offers=Count('company_name')) \
                                  .order_by('-count_offers')[:7]

    j_employment_type_counts = EmploymentTypes.objects.filter(id__in=junior_offers) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('type')

    m_employment_type_counts = EmploymentTypes.objects.filter(id__in=mid_offers) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('type')

    s_employment_type_counts = EmploymentTypes.objects.filter(id__in=senior_offers) \
        .values('type') \
        .annotate(count_type=Count('type')) \
        .order_by('type')

    context = {
        'j_employment_type_counts': j_employment_type_counts,
        'm_employment_type_counts': m_employment_type_counts,
        's_employment_type_counts': s_employment_type_counts,
        'j_positions_for_company': j_positions_for_company,
        'm_positions_for_company': m_positions_for_company,
        's_positions_for_company': s_positions_for_company,
        'junior_positions_month': junior_positions_month,
        'mid_positions_month': mid_positions_month,
        'senior_positions_month': senior_positions_month,
        'month': month,
        'positions_per_month': positions_per_month,
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
        'experience_level': experience_level,
        'work_type_office': work_type_office,
        'work_type_hybrid': work_type_hybrid,
        'work_type_remote': work_type_remote,
        'junior_positions': junior_positions,
        'mid_positions': mid_positions,
        'senior_positions': senior_positions,
        'min_avg1': min_avg1,
        'max_avg1': max_avg1,
        'min_avg2': min_avg2,
        'max_avg2': max_avg2,
        'min_avg3': min_avg3,
        'max_avg3': max_avg3,
        'min_avg4': min_avg4,
        'max_avg4': max_avg4,
        'min_avg5': min_avg5,
        'max_avg5': max_avg5,
        'min_avg6': min_avg6,
        'max_avg6': max_avg6,
        'min_avg7': min_avg7,
        'max_avg7': max_avg7,
    }
    return render(request, 'chart/quartal.html', context)


def start(request):
    return render(request, 'start.html')

def my_offers(request):

    my_offers = Offers.objects.filter(published_at__gte=seven_days_ago,
                      experience_level__in=['junior', 'mid'], marker_icon__in=['data', 'python'])

    context = {
        'my_offers': my_offers

    }
    return render(request, 'chart/my_offers.html', context)
