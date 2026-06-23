from django import forms

from meal.models import Meal, MealPlan, MealPlanItems, Ingredient, MealIngredients


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"


class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = "__all__"


class MealPlanItemsForm(forms.ModelForm):
    class Meta:
        model = MealPlanItems
        fields = "__all__"


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MealIngredientsForm(forms.ModelForm):
    class Meta:
        model = MealIngredients
        fields = "__all__"