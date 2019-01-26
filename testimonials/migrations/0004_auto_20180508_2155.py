# Generated by Django 2.0.4 on 2018-05-08 21:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_auto_20180508_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='text',
            field=tinymce.models.HTMLField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
