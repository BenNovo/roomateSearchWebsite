# Generated by Django 2.0.4 on 2018-04-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20180425_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomateuser',
            name='picture',
            field=models.ImageField(null=True, upload_to='ReubCxJUNOkZzn7D228d54a2-7d48-460f-aa1c-2826ecd4a350'),
        ),
    ]
