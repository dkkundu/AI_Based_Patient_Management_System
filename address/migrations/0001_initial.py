# Generated by Django 3.2 on 2021-06-10 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('dist_name', models.CharField(max_length=120)),
                ('dist_name_bn', models.CharField(blank=True, max_length=120, null=True)),
                ('dist_code', models.PositiveIntegerField(blank=True, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['dist_name'],
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('div_name', models.CharField(max_length=120)),
                ('div_name_bn', models.CharField(blank=True, max_length=120, null=True)),
                ('div_code', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['div_name'],
            },
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('upazila_name', models.CharField(max_length=120)),
                ('upazila_name_bn', models.CharField(blank=True, max_length=120, null=True)),
                ('upazila_code', models.PositiveIntegerField(blank=True, primary_key=True, serialize=False)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.district')),
            ],
            options={
                'ordering': ['upazila_name'],
            },
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.division'),
        ),
    ]
