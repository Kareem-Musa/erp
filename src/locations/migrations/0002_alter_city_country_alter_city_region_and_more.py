# Generated by Django 4.2.3 on 2023-07-28 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_cities', to='locations.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_cities', to='locations.region', verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_localities', to='locations.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_localities', to='locations.region', verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(blank=-1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_states', to='locations.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='state',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_states', to='locations.region', verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='unity',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country_unities', to='locations.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='unity',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region_unities', to='locations.region', verbose_name='Region'),
        ),
    ]
