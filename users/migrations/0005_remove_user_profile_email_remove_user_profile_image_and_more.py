# Generated by Django 4.0.4 on 2022-07-05 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='image',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_picture'),
        ),
    ]
