# Generated by Django 4.1 on 2022-09-09 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_news_data_category_alter_news_data_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news_data",
            name="date",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2022, 9, 9, 12, 12, 6, 171349, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]