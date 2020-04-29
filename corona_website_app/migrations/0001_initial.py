# Generated by Django 3.0.5 on 2020-04-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('num_cases', models.IntegerField()),
                ('num_recoveries', models.IntegerField()),
                ('num_deaths', models.IntegerField()),
            ],
        ),
    ]