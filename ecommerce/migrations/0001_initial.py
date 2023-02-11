# Generated by Django 3.2.16 on 2023-02-11 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_amount', models.FloatField(verbose_name='Products amount')),
                ('delivery_amount', models.FloatField(verbose_name='Delivery amount')),
                ('total_amount', models.FloatField(verbose_name='Total amount')),
                ('active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('score', models.IntegerField(verbose_name='Score')),
                ('image', models.ImageField(upload_to='media/product_images/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_checkout', models.DateField(verbose_name='Date of checkout')),
                ('cart', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.cart', verbose_name='Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='ecommerce.Product', verbose_name='Products'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cart owner'),
        ),
    ]
