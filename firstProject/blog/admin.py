from django.contrib import admin
from blog.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'update', 'timestamp', 'price', 'topic')
    list_display_links = ('update', )
    list_editable = ('title', 'topic')
    list_filter = ('update', 'timestamp', 'topic')
    # Обмежемо максимальну кількість постів на сторінці щоб лаконічно виглядало
    # та не потрібно було скорилити бескінечно при великій кількості постів
    # максисальна кількість постів на сторінці буде 10 і при більшій кількості
    # постів створюються додаткові сторінки
    list_per_page = 10
    # Використаємо поле для пошуку поста в даному випадку по назві
    # Пошук потрібний, для зручнішого користування та швидкого пошуку поста якщо ми знаємо його назву
    search_fields = ('title',)


admin.site.register(Post, PostModelAdmin)


