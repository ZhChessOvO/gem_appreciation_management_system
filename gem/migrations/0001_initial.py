# Generated by Django 2.0.3 on 2020-11-23 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shouyang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testNo', models.CharField(default=-1, max_length=20)),
                ('tel', models.CharField(default=-1, max_length=20)),
                ('testSituation', models.CharField(default=-1, max_length=20)),
                ('testCompany', models.CharField(default=-1, max_length=20)),
                ('testNum', models.CharField(default=-1, max_length=20)),
                ('kuangNo', models.CharField(default=-1, max_length=20)),
                ('time', models.CharField(default=-1, max_length=20)),
                ('paid', models.CharField(default=-1, max_length=4)),
            ],
        ),
    ]