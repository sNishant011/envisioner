# Generated by Django 3.1 on 2020-08-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Video', '0005_auto_20200814_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='categories',
            name='parent',
            field=models.ManyToManyField(blank=True, default=None, to='Video.Description'),
        ),
    ]
