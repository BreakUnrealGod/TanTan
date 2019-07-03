# Generated by Django 2.2.3 on 2019-07-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=11, unique=True)),
                ('nickname', models.CharField(max_length=32)),
                ('sex', models.IntegerField(default=0)),
                ('birth_yaer', models.IntegerField(default=2000)),
                ('birth_mohth', models.IntegerField(default=1)),
                ('birth_day', models.IntegerField(default=1)),
                ('avatar', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
