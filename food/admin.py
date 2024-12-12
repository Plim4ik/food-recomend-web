from django.contrib import admin
from .models import Category, Filter, Food

class FilterInline(admin.TabularInline):
    model = Filter
    extra = 1  # Количество пустых полей для добавления новых фильтров


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Отображение имени и описания категории
    search_fields = ('name', 'description')  # Добавляем поиск по имени и описанию
    inlines = [FilterInline]  # Добавляем Inline для фильтров


class FoodInline(admin.TabularInline):
    model = Food.filters.through  # Связь через ManyToMany
    extra = 1  # Количество пустых полей для добавления фильтров


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Отображение основных полей
    list_filter = ('filters__category',)  # Фильтрация по категориям фильтров
    search_fields = ('name', 'description')  # Поиск по имени и описанию
    autocomplete_fields = ('filters',)  # Удобный выбор фильтров через поиск

@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Отображение фильтра и категории
    list_filter = ('category',)  # Фильтрация по категории
    search_fields = ('name',)  # Поиск по имени
