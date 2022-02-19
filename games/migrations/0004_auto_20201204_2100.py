# Generated by Django 3.1.3 on 2020-12-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20201204_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='cpu',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='gpu',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='hdd',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='os',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='ram',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]