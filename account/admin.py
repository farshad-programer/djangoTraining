from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_enable",
        "publish_date",
        "created_time",
        "updated_time",
    )
    list_filter = ("is_enable", "publish_date")
    search_fields = ("title", "text")
    date_hierarchy = "publish_date"
    ordering = ("-publish_date",)
