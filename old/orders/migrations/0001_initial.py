# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(unique=True)),
                ('order_date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_status', models.CharField(max_length=30)),
                ('original_price', models.FloatField()),
                ('price', models.FloatField()),
                ('qty', models.IntegerField(default=1)),
                ('subtotal', models.FloatField()),
                ('tax_amount', models.FloatField(default=0)),
                ('discount_amount', models.FloatField(default=0)),
                ('row_total', models.FloatField()),
                ('renew_duration', models.DurationField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='subscription_flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('customer_name', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=300)),
                ('order_id', models.CharField(max_length=150)),
                ('order_item_id', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=30)),
                ('requiring_duration', models.DurationField(default=0)),
                ('start_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='subscription_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('SUSPENDED', 'Sunpended'), ('HOLD', 'Hold')], default='ACTIVE', max_length=30)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order_item')),
            ],
        ),
        migrations.CreateModel(
            name='subscription_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('requiring_duration', models.DurationField(default=0)),
                ('price', models.FloatField(default=0)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('SUSPENDED', 'Sunpended'), ('HOLD', 'Hold')], default='ACTIVE', max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order_status'),
        ),
    ]
