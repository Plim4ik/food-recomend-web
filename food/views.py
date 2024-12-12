from django.shortcuts import render
from .models import Food, Category
import random

def food_list(request):
    filters = request.GET.getlist('filters', [])
    random_food = request.GET.get('random', None)
    foods = Food.objects.all()

    if random_food:
        # Рандомное блюдо
        foods = [random.choice(foods)] if foods.exists() else []
    elif filters:
        # Фильтрация по выбранным фильтрам
        foods = foods.filter(filters__id__in=filters).distinct()

    categories = Category.objects.prefetch_related('filters')

    return render(request, 'food_list.html', {
        'foods': foods,
        'categories': categories,
        'selected_filters': filters,
    })
