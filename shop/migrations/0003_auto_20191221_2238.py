# Generated by Django 3.0 on 2019-12-21 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191221_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='upcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.UpCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
        ),
    ]