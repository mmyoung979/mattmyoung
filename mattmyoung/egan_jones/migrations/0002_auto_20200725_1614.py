# Generated by Django 3.0.7 on 2020-07-25 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egan_jones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statementofcashflows',
            name='date_pulled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 25, 16, 14, 56, 704509)),
        ),
    ]