from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from meal.models import Meal, MealIngredients, Ingredient
from meal.forms import MealForm, MealIngredientsForm, MealIngredients, IngredientForm, MealPlanForm, MealPlan
from meal.service import generate_data
import json 
import ollama

class MealView(ListView):
    model = Meal
    template_name = 'meal/index.html'
    context_object_name = 'meal'

class MealCreateView(CreateView):
    model = Meal
    template_name = 'meal/create.html'
    form_class = MealForm
    success_url = '/meal'

class MealUpdateView(UpdateView):   
    model = Meal
    template_name = 'meal/create.html'
    form_class = MealForm
    success_url = '/meal'

class MealDeleteView(DeleteView):
    model=Meal
    success_url = '/meal'




class IngredientListView(ListView):
    model = Ingredient
    paginate_by = 10
    template_name = "ingredient/ingredient_list.html"


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/create.html"
    success_url = "/meal/ingredients/"


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/update.html"
    success_url = "/meal/ingredients/"


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "ingredient/delete.html"
    success_url = "/meal/ingredients/"


class MealPlanView(ListView):
    model = MealPlan
    paginate_by = 10
    template_name = 'mealPlan/index.html'
    context_object_name = 'mealPlan'


class MealPlanCreateView(CreateView):
    model=MealPlan
    template_name = 'mealPlan/create.html'
    form_class = MealPlanForm
    success_url = '/meal/plan/list'


class MealPlanUpdateView(UpdateView):
    model=MealPlan
    template_name = 'mealPlan/update.html'
    form_class = MealPlanForm
    success_url = '/meal/plan/list'


class MealPlanDeleteView(DeleteView):
    model = MealPlan
    template_name = 'mealPlan/delete.html'
    success_url = '/meal/plan/list'

class MealIngredientsView(ListView):
    model = MealIngredients
    paginate_by = 10
    template_name = 'meal/ingredients.html'
    context_object_name = 'ingredients'


class MealIngredientsCreateView(CreateView):
    model = MealIngredients
    template_name = 'meal/ingredients_create.html'
    form_class = MealIngredientsForm
    success_url = '/meal/ingredients/'


class MealIngredientsUpdateView(UpdateView):
    model = MealIngredients
    template_name = 'meal/ingredients_update.html'
    form_class = MealIngredientsForm
    success_url = '/meal/ingredients/'


class MealIngredientsDeleteView(DeleteView):
    model = MealIngredients
    template_name = 'meal/ingredients_delete.html'
    success_url = '/meal/ingredients/'


def generate_ai_data(request):
    data = generate_data()
    print(json.loads(data))
    return render(request,'ingredient/ai.html', context={"data":data})