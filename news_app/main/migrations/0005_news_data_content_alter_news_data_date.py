# Generated by Django 4.1 on 2022-08-20 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_news_data_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="news_data",
            name="content",
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="news_data",
            name="date",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2022, 8, 20, 17, 43, 37, 26386, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]
