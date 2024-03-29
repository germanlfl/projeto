# Generated by Django 2.2.1 on 2019-05-25 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('alias', models.SlugField(max_length=255, primary_key=True, serialize=False)),
                ('domain', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('count', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['count'],
            },
        ),
    ]
