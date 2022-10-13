# Generated by Django 3.2.16 on 2022-10-13 21:03

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('PSR', 'Poolside'), ('GVR', 'Garden View'), ('OVR', 'Ocean View'), ('SOS', 'Superior Ocean Suite')], max_length=3)),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_adults', models.IntegerField(choices=[(1, '1 adult'), (2, '2 adults')], default=1)),
                ('num_children', models.IntegerField(choices=[(0, '0 children'), (1, '1 child'), (2, '2 children')], default=0)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.customer')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
