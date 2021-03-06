# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.CharField(max_length=31, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'batches',
            },
        ),
        migrations.CreateModel(
            name='MeasurementCorrection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.CharField(max_length=31)),
                ('correction_factor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_result', models.CharField(max_length=63)),
                ('round_inner_bright_area', models.IntegerField()),
                ('round_inner_large_dark_area', models.IntegerField()),
                ('round_inner_small_dark_area', models.IntegerField()),
                ('round_outer_bright_area', models.IntegerField()),
                ('round_outer_large_dark_area', models.IntegerField()),
                ('round_outer_small_dark_area', models.IntegerField()),
                ('flat_inner_diameter_min', models.IntegerField()),
                ('flat_inner_diameter_max', models.IntegerField()),
                ('flat_obstruction_area', models.IntegerField()),
                ('flat_chip_area', models.IntegerField()),
                ('dimension_length_mm', models.IntegerField()),
                ('dimension_bump_max', models.IntegerField()),
                ('dimension_chip_max', models.IntegerField()),
                ('dimension_envelope_mm', models.IntegerField()),
                ('dimension_nose_min_max', models.IntegerField()),
                ('dimension_median_od', models.IntegerField()),
                ('sepia_bright_area', models.IntegerField()),
                ('sepia_blemish_area', models.IntegerField()),
                ('sepia_spot_crack_area', models.IntegerField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary_report.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementMean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_result', models.CharField(max_length=63)),
                ('round_inner_bright_area', models.FloatField()),
                ('round_inner_large_dark_area', models.FloatField()),
                ('round_inner_small_dark_area', models.FloatField()),
                ('round_outer_bright_area', models.FloatField()),
                ('round_outer_large_dark_area', models.FloatField()),
                ('round_outer_small_dark_area', models.FloatField()),
                ('flat_inner_diameter_min', models.FloatField()),
                ('flat_inner_diameter_max', models.FloatField()),
                ('flat_obstruction_area', models.FloatField()),
                ('flat_chip_area', models.FloatField()),
                ('dimension_length_mm', models.FloatField()),
                ('dimension_bump_max', models.FloatField()),
                ('dimension_chip_max', models.FloatField()),
                ('dimension_envelope_mm', models.FloatField()),
                ('dimension_nose_min_max', models.FloatField()),
                ('dimension_median_od', models.FloatField()),
                ('sepia_bright_area', models.FloatField()),
                ('sepia_blemish_area', models.FloatField()),
                ('sepia_spot_crack_area', models.FloatField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary_report.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.CharField(max_length=31)),
                ('min', models.FloatField(blank=True)),
                ('max', models.FloatField(blank=True)),
                ('nominal', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StandardID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=31, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('inspected', models.IntegerField()),
                ('good', models.IntegerField()),
                ('good_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fail_general', models.IntegerField()),
                ('fail_gen_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fail_od', models.IntegerField()),
                ('fail_od_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fail_backward', models.IntegerField()),
                ('fail_backward_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('n_a', models.IntegerField()),
                ('n_a_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gate_homes', models.IntegerField()),
                ('lost_homing', models.IntegerField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary_report.Batch')),
            ],
            options={
                'verbose_name_plural': 'summaries',
            },
        ),
        migrations.CreateModel(
            name='TestPassPercent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_result', models.CharField(max_length=63)),
                ('round_end', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flat_end', models.DecimalField(decimal_places=2, max_digits=5)),
                ('outer_dimension', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sepia_screen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_valid_master', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_valid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_present', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_orientation', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_inner_bright', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_outer_bright', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_inner_small_dark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_outer_small_dark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_inner_large_dark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('round_outer_large_dark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flat_valid_master', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flat_orientation', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flat_valid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flat_ID', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flat_obstruction', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flat_chip', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dimension_position', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dimension_length', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dimension_bumps', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dimension_chips', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dimension_envelope', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dimension_nose', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sepia_valid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sepia_bright_spot', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sepia_blemish', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sepia_spot_crack', models.DecimalField(decimal_places=2, max_digits=5)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary_report.Batch')),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary_report.Summary')),
            ],
        ),
        migrations.AddField(
            model_name='measurementstandard',
            name='standard_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary_report.StandardID'),
        ),
        migrations.AddField(
            model_name='measurementmean',
            name='summary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary_report.Summary'),
        ),
        migrations.AddField(
            model_name='measurementcount',
            name='summary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary_report.Summary'),
        ),
    ]
