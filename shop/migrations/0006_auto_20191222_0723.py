# Generated by Django 3.0 on 2019-12-22 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20191222_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='upcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.UpCategory', unique=True),
        ),
    ]
