# Generated by Django 3.2.23 on 2023-12-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('imgs', models.ImageField(upload_to='pic')),
                ('descs', models.TextField()),
            ],
        ),
    ]
