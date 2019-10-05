# Generated by Django 2.2.6 on 2019-10-04 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=30)),
                ('in_stock_qty', models.IntegerField(default=0)),
                ('out_of_stock', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='product_category', to='products.Category')),
                ('sub_categories', models.ManyToManyField(blank=True, related_name='product_subcategory', to='products.SubCategory')),
            ],
        ),
    ]
