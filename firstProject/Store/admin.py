from django.contrib import admin
from Store.models import CreateProduct
from django.utils.safestring import mark_safe

# модель створення продукту
class CreateProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'display_image', 'price', 'time_create', 'id')
    list_editable = ('topic',)
    search_fields = ('title', )
    list_filter = ('time_create', 'topic')
    list_per_page = 10

    # відображення картинки в адміністративному інтерфейсі
    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')


    display_image.short_description = 'Image'  # Заголовок ствпця з зображенням

admin.site.register(CreateProduct, CreateProductAdmin)
