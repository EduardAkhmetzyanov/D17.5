# Generated by Django 4.2.4 on 2023-10-22 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_category_subscribers_alter_news_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers_en_us',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers_ru',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='category_en_us',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.AddField(
            model_name='news',
            name='category_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='news.category'),
        ),
        migrations.AddField(
            model_name='news',
            name='description_en_us',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='name_en_us',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='news',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='news',
            name='time_create_en_us',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='news',
            name='time_create_ru',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
    ]
