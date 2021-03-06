# Generated by Django 4.0.4 on 2022-06-13 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_and_brand', '0005_alter_brandpromotion_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandpromotion',
            name='plan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='customer_and_brand.plan'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('BP', 'Brand Partner'), ('EU', 'End User')], default='EU', max_length=2, verbose_name='Type of user'),
        ),
    ]
