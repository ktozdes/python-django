# Generated by Django 3.2.4 on 2021-06-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210623_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]