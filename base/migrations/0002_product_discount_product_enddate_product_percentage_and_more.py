# Generated by Django 4.2.6 on 2023-10-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
