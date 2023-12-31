# Generated by Django 4.2.3 on 2023-07-28 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Country Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Locality Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_localities', to='locations.country', verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Localities',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Region Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Regions',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='State Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_states', to='locations.country', verbose_name='Country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_states', to='locations.region', verbose_name='Region')),
            ],
            options={
                'verbose_name_plural': 'States',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Unity Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_unities', to='locations.country', verbose_name='Country')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locality_unities', to='locations.locality', verbose_name='Locality')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_unities', to='locations.region', verbose_name='Region')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_unities', to='locations.state', verbose_name='State')),
            ],
            options={
                'verbose_name_plural': 'Unities',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='locality',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_localities', to='locations.region', verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='locality',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_localities', to='locations.state', verbose_name='State'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_countries', to='locations.region', verbose_name='Region'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Unity Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_cities', to='locations.country', verbose_name='Country')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locality_cities', to='locations.locality', verbose_name='Locality')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_cities', to='locations.region', verbose_name='Region')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_cities', to='locations.state', verbose_name='State')),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'ordering': ['created'],
            },
        ),
    ]
