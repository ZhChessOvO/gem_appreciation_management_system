# Generated by Django 2.0.3 on 2020-12-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gem', '0007_yangpin_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='vip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='未填写', max_length=20)),
                ('tel', models.CharField(default='未填写', max_length=20)),
                ('type', models.CharField(default='未填写', max_length=10)),
                ('people', models.CharField(default='未填写', max_length=20)),
                ('number', models.CharField(default='未填写', max_length=20)),
                ('mail', models.CharField(default='未填写', max_length=20)),
                ('company', models.CharField(default='未填写', max_length=20)),
                ('address', models.CharField(default='未填写', max_length=20)),
            ],
        ),
    ]
