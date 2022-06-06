# Generated by Django 4.0.4 on 2022-06-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('duracioncapitulos', models.IntegerField()),
                ('actores', models.CharField(max_length=100)),
                ('creacion', models.IntegerField()),
                ('SKU', models.CharField(max_length=30, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'serie',
                'verbose_name_plural': 'series',
            },
        ),
    ]
