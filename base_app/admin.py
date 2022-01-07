from django.contrib import admin
from .models import Home, Service, Dish, CategoryDish, About, BookTable, Chef, Feedback

admin.site.register(Home)
admin.site.register(Service)
admin.site.register(About)
admin.site.register(BookTable)
admin.site.register(Chef)
admin.site.register(Feedback)


class DishAdmin(admin.TabularInline):
    model = Dish
    row_id_fields = ['name']


@admin.register(CategoryDish)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    inlines = [DishAdmin]
