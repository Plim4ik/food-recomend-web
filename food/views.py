from django.shortcuts import render, get_object_or_404
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


def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'food_detail.html', {'food': food})
