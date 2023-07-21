from django.urls import path, include
from . import views

urlpatterns = [
    path('day_selection/', views.home_view, name='day_selection'),
    path('day_selection/submitted/', views.submit_day_selection_view, name='submitted'),
    path('availabilities/', views.all_availabilities, name='all_availabilities'),
]
