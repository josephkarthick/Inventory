# Generated by Django 4.1.5 on 2023-01-29 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='productmovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_id', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_location', models.CharField(max_length=50)),
                ('to_location', models.CharField(max_length=50)),
                ('qyt', models.CharField(max_length=50)),
                ('Product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.product')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.location')),
            ],
        ),
    ]