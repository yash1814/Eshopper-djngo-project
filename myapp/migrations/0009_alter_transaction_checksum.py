# Generated by Django 4.1.6 on 2023-03-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='checksum',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
