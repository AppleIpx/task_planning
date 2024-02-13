from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="название категории",
    )

    def __str__(self):
        return self.name


class TaskPlan(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Заголовок",
        blank=False,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name="текст"
    )
    deadline = models.DateTimeField(
        verbose_name="Крайний срок выполнения",
    )
    categories = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    is_it_ready = models.BooleanField(
        verbose_name="Флаг выполнения задания",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )

    def __str__(self):
        return self.title