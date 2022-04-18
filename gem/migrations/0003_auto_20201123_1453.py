# Generated by Django 2.0.3 on 2020-11-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gem', '0002_shouyang_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yangpin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testNo', models.CharField(default='未填写', max_length=20)),
                ('situation', models.CharField(default='未填写', max_length=20)),
                ('no', models.CharField(default='未填写', max_length=10)),
                ('result', models.CharField(default='未填写', max_length=20)),
                ('appear', models.CharField(default='未填写', max_length=20)),
                ('weight', models.CharField(default='未填写', max_length=20)),
                ('midu', models.CharField(default='未填写', max_length=20)),
                ('zheshe', models.CharField(default='未填写', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='kuangNo',
            field=models.CharField(default='未填写', max_length=20),
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='money',
            field=models.CharField(default='未填写', max_length=10),
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='paid',
            field=models.CharField(default='未填写', max_length=4),
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='tel',
            field=models.CharField(default='未填写', max_length=20),
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='testCompany',
            field=models.CharField(default='未填写', max_length=20),
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='testNo',
            field=models.CharField(default='未填写', max_length=20),
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='testNum',
            field=models.CharField(default='未填写', max_length=20),
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='testSituation',
            field=models.CharField(default='未填写', max_length=20),
        ),
        migrations.AlterField(
            model_name='shouyang',
            name='time',
            field=models.CharField(default='未填写', max_length=20),
        ),
    ]