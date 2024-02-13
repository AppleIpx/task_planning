from django.contrib import admin
from django.contrib.admin import register
from .models import (
    TaskPlan,
    Category,
)


admin.site.register(Category)


@register(TaskPlan)
class TaskPlanAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'categories',
        'deadline',
        'is_it_ready',
        'created_at',
    )
    list_filter = (
        'title',
        'created_at',
    )
