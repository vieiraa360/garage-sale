# Generated by Django 2.0.4 on 2018-05-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0006_auto_20180511_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
