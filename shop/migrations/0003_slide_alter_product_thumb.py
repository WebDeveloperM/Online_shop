# Generated by Django 4.0.1 on 2022-04-25 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_user_product_thumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='slide.jpg', upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='thumb',
            field=models.ImageField(default='no_product.png', null=True, upload_to='images/'),
        ),
    ]
