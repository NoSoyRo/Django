# Generated by Django 4.1.7 on 2023-03-06 15:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_feed_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.species')),
            ],
        ),
    ]