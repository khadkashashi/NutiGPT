from django.urls import path
from .views import MealCreateView, MealDeleteView, MealUpdateView, MealView


urlpatterns = [
    path('', MealView.as_view(), name="meal-list"),
    path('create/', MealCreateView.as_view(), name="meal-create"),
    path('update/<int:pk>/', MealUpdateView.as_view(), name="meal-update"),
    path('delete/<int:pk>/', MealDeleteView.as_view(), name="meal-delete"),
]