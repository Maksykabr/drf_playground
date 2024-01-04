# Generated by Django 5.0 on 2023-12-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('surname', models.CharField(db_index=True, max_length=150)),
                ('birthday', models.DateField()),
                ('specialty', models.CharField(db_index=True, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('university', models.ManyToManyField(to='drf_app.university')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('surname', models.CharField(db_index=True, max_length=150)),
                ('birthday', models.DateField()),
                ('specialty', models.CharField(db_index=True, max_length=150)),
                ('course', models.IntegerField(choices=[(1, 'Active'), (2, 'Inactive'), (3, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('university', models.ManyToManyField(to='drf_app.university')),
            ],
        ),
    ]