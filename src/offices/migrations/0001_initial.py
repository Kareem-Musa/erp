# Generated by Django 4.2.3 on 2023-07-28 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hquarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Hquarter Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_countries', to='locations.country', verbose_name='Country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_hquarters', to='locations.region', verbose_name='Region')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_hquarters', to='locations.state', verbose_name='State')),
            ],
            options={
                'verbose_name_plural': 'Hquarters',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Sector Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hquarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hquarter_sectors', to='offices.hquarter', verbose_name='Hquarter')),
            ],
            options={
                'verbose_name_plural': 'Sectors',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Office Name')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hquarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hquarter_offices', to='offices.hquarter', verbose_name='Hquarter')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_offices', to='offices.sector', verbose_name='Sector')),
            ],
            options={
                'verbose_name_plural': 'Offices',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Epoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Entry Point')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Hquarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hquarter_epoints', to='offices.hquarter', verbose_name='Hquarter')),
                ('Sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sector_epoints', to='offices.sector', verbose_name='Sector')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='office_epoints', to='offices.office', verbose_name='Office')),
            ],
            options={
                'verbose_name_plural': 'Epoints',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Cpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Collection Point')),
                ('slug', models.SlugField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Hquarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hquarter_cpoints', to='offices.hquarter', verbose_name='Hquarter')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='office_cpoints', to='offices.office', verbose_name='Office')),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sector_cpionts', to='offices.sector', verbose_name='Sector')),
            ],
            options={
                'verbose_name_plural': 'Hquarters',
                'ordering': ['created'],
            },
        ),
    ]