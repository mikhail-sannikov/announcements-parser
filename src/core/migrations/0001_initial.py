# Generated by Django 5.0.6 on 2024-06-28 02:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='название')),
            ],
            options={
                'verbose_name': 'компания',
                'verbose_name_plural': 'компании',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='заголовок')),
                ('views_amount', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
                ('position', models.PositiveSmallIntegerField(db_index=True, unique=True, verbose_name='позиция в списке')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='core.company', verbose_name='компания')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='CompanyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(verbose_name='дата устройства')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies_members', to='core.company', verbose_name='компания')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies_members', to=settings.AUTH_USER_MODEL, verbose_name='сотрудник')),
            ],
            options={
                'verbose_name': 'сотрудник компании',
                'verbose_name_plural': 'сотрудники компаний',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='members',
            field=models.ManyToManyField(related_name='companies', through='core.CompanyMember', to=settings.AUTH_USER_MODEL, verbose_name='участники'),
        ),
    ]
