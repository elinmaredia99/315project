# Generated by Django 3.0.5 on 2020-04-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health',
            fields=[
                ('calories', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'health',
                'managed': False,
            },
        ),
    ]
