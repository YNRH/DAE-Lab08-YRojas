# Generated by Django 3.2 on 2023-05-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='category',
            field=models.CharField(choices=[('horror', 'Horror'), ('comedy', 'Comedy'), ('action', 'Action'), ('drama', 'Drama'), ('aventura', 'aventura')], max_length=10),
        ),
    ]