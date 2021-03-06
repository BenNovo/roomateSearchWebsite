# Generated by Django 2.0.4 on 2018-04-23 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomateUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('answer_one', models.CharField(max_length=30)),
                ('answer_two', models.CharField(max_length=30)),
                ('answer_three', models.CharField(max_length=30)),
                ('answer_four', models.CharField(max_length=30)),
                ('answer_five', models.CharField(max_length=30)),
            ],
        ),
    ]
