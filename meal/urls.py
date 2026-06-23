from django.urls import path
from meal.views import MealView
urlpatterns = [
    path('',MealView.as_view(),name="meal-view"),
]