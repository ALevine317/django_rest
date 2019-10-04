# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-09 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('brandname', models.CharField(max_length=30)),
                ('material', models.CharField(max_length=30)),
                ('fasten_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='shoe',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ShoeColor'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Manufacturer'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoe_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ShoeType'),
        ),
    ]
