# Generated by Django 3.1.2 on 2020-11-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True,
                primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price_per_box', models.DecimalField(decimal_places=2,
                                             max_digits=6)),
            ],
        ),
    ]
