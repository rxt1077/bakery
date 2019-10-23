# Generated by Django 2.2.5 on 2019-10-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookie',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=6),
            preserve_default=False,
        ),
    ]