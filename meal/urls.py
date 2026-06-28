from django.urls import path

from .views import MealCreateView, MealDeleteView, MealUpdateView, MealView,     MealIngredientsView, MealIngredientsCreateView, MealIngredientsUpdateView, MealIngredientsDeleteView, MealIngredients

from .views import MealCreateView, MealDeleteView, MealUpdateView, MealView, IngredientListView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView

from .views import MealCreateView, MealDeleteView, MealPlanCreateView, MealPlanDeleteView, MealPlanUpdateView, MealPlanView, MealUpdateView, MealView

urlpatterns = [
    path('', MealView.as_view(), name="meal-list"),
    path('create/', MealCreateView.as_view(), name="meal-create"),
    path('update/<int:pk>/', MealUpdateView.as_view(), name="meal-update"),
    path('delete/<int:pk>/', MealDeleteView.as_view(), name="meal-delete"),
    path('ingredients/', MealIngredientsView.as_view(), name='ingredients-list'),
    path('ingredients/create/', MealIngredientsCreateView.as_view(), name='ingredients-create'),
    path('ingredients/update/<pk>/', MealIngredientsUpdateView.as_view(), name='ingredients-update'),
    path('ingredients/delete/<pk>/', MealIngredientsDeleteView.as_view(), name='ingredients-delete'),
  path("ingredients/",IngredientListView.as_view(),name="ingredient-list"),
    path("ingredients/create/",IngredientCreateView.as_view(),name="ingredient-create"),
    path("ingredients/update/<int:pk>/",IngredientUpdateView.as_view(),name="ingredient-update"),
    path("ingredients/delete/<int:pk>/",IngredientDeleteView.as_view(),name="ingredient-delete"),


    path('plan/list', MealPlanView.as_view(), name="mealplan-list"),
    path('plan/create/', MealPlanCreateView.as_view(), name='mealplan-create'),
    path('plan/update/<int:pk>/', MealPlanUpdateView.as_view(), name='mealplan-update'),
    path('plan/delete/<int:pk>/', MealPlanDeleteView.as_view(), name='mealplan-delete'),


]