from django.shortcuts import render
from meal.models import Meal, MealIngredients, MealPlan, MealPlanItems, Ingredient

# Create your views here.


def dashboard(request):
    meal = Meal.objects.all()
    meal_ingredient = MealIngredients.objects.all()
    meal_plan = MealPlan.objects.all()
    meal_plan_items = MealPlanItems.objects.all()
    ingredient = Ingredient.objects.all()


    context = {
    "cards": [
        {"title": "Meals", "count": meal.count()},
        {"title": "Meal Ingredients", "count": meal_ingredient.count()},
        {"title": "Meal Plans", "count": meal_plan.count()},
    ]
}

    return render(request,'home/base.html',context)