# Generated by Django 5.0 on 2023-12-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
                ('date_create', models.DateField(blank=True, null=True, verbose_name='date_create')),
                ('change_data', models.DateField(blank=True, null=True, verbose_name='change_data')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]