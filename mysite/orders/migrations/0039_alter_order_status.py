# Generated by Django 4.0.5 on 2022-07-07 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0038_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Accepted', 'Accepted')], default='New', max_length=15),
        ),
    ]