# Generated by Django 3.0.7 on 2020-07-23 23:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatementOfCashFlows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=5)),
                ('table', models.TextField()),
                ('date_pulled', models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 19, 40, 39, 289035))),
            ],
        ),
    ]
