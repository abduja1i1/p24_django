from django.urls import path

from course.views import subject_list, speciality_list, speciality_detail, home

urlpatterns = [
    path('subjects/', subject_list, name="subjects"),
    path('specialities/', speciality_list, name="specialites"),
    path('speciality/<id>/', speciality_detail, name="speciality"),
    path('', home, name="home"),
]