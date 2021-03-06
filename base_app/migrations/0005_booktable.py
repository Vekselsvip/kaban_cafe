# Generated by Django 3.2.9 on 2022-01-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField(max_length=150)),
                ('people', models.PositiveIntegerField()),
                ('is_processed', models.BooleanField(default=False)),
            ],
        ),
    ]
