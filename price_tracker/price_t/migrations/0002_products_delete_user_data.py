# Generated by Django 4.0.4 on 2023-07-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_t', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_name', models.CharField(max_length=50)),
                ('product_url', models.URLField(primary_key=True, serialize=False, unique=True)),
                ('product_price', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='user_data',
        ),
    ]
