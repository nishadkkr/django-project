# Generated by Django 4.0.5 on 2022-07-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0036_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Failed', 'Failed'), ('Completed', 'Completed'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled')], default='New', max_length=15),
        ),
    ]