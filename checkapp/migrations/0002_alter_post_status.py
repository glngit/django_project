# Generated by Django 4.0.8 on 2023-02-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]
