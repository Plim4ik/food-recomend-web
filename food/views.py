from django.shortcuts import render, get_object_or_404
from .models import Food, Category
from django.db.models import Count
import random

def food_list(request):
    filters = request.GET.getlist('filters', [])  # Получаем список выбранных фильтров
    random_food = request.GET.get('random', None)  # Проверяем, запрошено ли случайное блюдо
    foods = Food.objects.all()

    if random_food:
        # Рандомное блюдо без учета фильтров
        foods = [random.choice(list(foods))] if foods.exists() else []
    elif filters:
        # Строгое соответствие всем выбранным фильтрам
        filter_count = len(filters)  # Количество выбранных фильтров
        foods = foods.filter(filters__id__in=filters)
        foods = foods.annotate(filter_match_count=Count('filters', distinct=True))
        foods = foods.filter(filter_match_count=filter_count)

    categories = Category.objects.prefetch_related('filters')

    return render(request, 'food_list.html', {
        'foods': foods,
        'categories': categories,
        'selected_filters': filters,
    })



def food_detail(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    return render(request, 'food_detail.html', {'food': food})
