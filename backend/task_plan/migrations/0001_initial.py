# Generated by Django 5.0.2 on 2024-02-12 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='название категории')),
            ],
        ),
        migrations.CreateModel(
            name='TaskPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='текст')),
                ('deadline', models.DateTimeField(verbose_name='Крайний срок выполнения')),
                ('is_it_ready', models.BooleanField(verbose_name='Флаг выполнения задания')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('categories', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='task_plan.category')),
            ],
        ),
    ]
