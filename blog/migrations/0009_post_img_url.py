# Generated by Django 3.1 on 2020-08-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_url',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
