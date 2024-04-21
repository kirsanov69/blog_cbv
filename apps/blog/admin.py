from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Post, Category, Comment, Rating

# Register your models here.

@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель для категорий
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    АДмин-панель для постов
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdminPage(DjangoMpttAdmin):
    """
    Админ-панель для комментариев
    """
    pass

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Админ-панель для рейтинга
    """
    pass