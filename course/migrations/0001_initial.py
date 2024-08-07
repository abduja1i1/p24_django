# Generated by Django 5.0.7 on 2024-07-25 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=56)),
                ('last_name', models.CharField(max_length=56)),
                ('username', models.CharField(max_length=56)),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='course.speciality')),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=56)),
                ('address', models.TextField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='course.student')),
            ],
        ),
        migrations.AddField(
            model_name='speciality',
            name='subjects',
            field=models.ManyToManyField(to='course.subject'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=56)),
                ('last_name', models.CharField(max_length=56)),
                ('email', models.EmailField(max_length=56)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=26)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('subjects', models.ManyToManyField(related_name='teachers', to='course.subject')),
            ],
        ),
    ]
