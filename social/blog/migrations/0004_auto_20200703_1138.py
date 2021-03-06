# Generated by Django 3.0.7 on 2020-07-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_src',
            field=models.ImageField(default='noimage.png', upload_to='uploads/'),
        ),
    ]
