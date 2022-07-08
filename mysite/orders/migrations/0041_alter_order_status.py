# Generated by Django 4.0.5 on 2022-07-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0040_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], default='New', max_length=15),
        ),
    ]