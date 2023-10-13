# Generated by Django 4.0.1 on 2023-10-13 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_rename_product_date_color_color_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('roll_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('length', models.FloatField()),
                ('measurement_unit', models.CharField(choices=[('m', 'meter'), ('y', 'yard')], max_length=64)),
                ('location', models.CharField(max_length=64, null=True)),
                ('color_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('sold', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='color',
            old_name='colorKey',
            new_name='typeKey',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='colorOfType',
            new_name='typeOfProduct',
        ),
        migrations.RemoveField(
            model_name='color',
            name='color_date',
        ),
        migrations.RemoveField(
            model_name='color',
            name='length',
        ),
        migrations.RemoveField(
            model_name='color',
            name='location',
        ),
        migrations.RemoveField(
            model_name='color',
            name='measurement_unit',
        ),
        migrations.RemoveField(
            model_name='color',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='type',
            name='product',
        ),
        migrations.AddField(
            model_name='color',
            name='colorOfType',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='roll',
            name='colorKey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.color'),
        ),
        migrations.AddField(
            model_name='order',
            name='roll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.roll'),
        ),
    ]
