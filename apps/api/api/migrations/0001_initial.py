# Generated by Django 4.2.3 on 2023-11-18 00:12

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('line_one', models.CharField(max_length=64)),
                ('line_two', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=16)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ConeType',
            fields=[
                ('name', models.CharField(max_length=128,
                 primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('unit_cost', models.PositiveIntegerField()),
                ('image_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.CharField(
                    max_length=64, primary_key=True, serialize=False)),
                ('password_hash', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DroneStatus',
            fields=[
                ('text', models.CharField(max_length=32,
                 primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DroneType',
            fields=[
                ('text', models.CharField(max_length=32,
                 primary_key=True, serialize=False)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IceCreamType',
            fields=[
                ('name', models.CharField(max_length=128,
                 primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('unit_cost', models.PositiveIntegerField()),
                ('image_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('username', models.CharField(
                    max_length=64, primary_key=True, serialize=False)),
                ('password_hash', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ManagerCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('message', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerRevenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('message', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('cost', models.PositiveIntegerField()),
                ('delivered_at', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.address')),
                ('customer', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.PROTECT, to='api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('text', models.CharField(max_length=32,
                 primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('username', models.CharField(
                    max_length=64, primary_key=True, serialize=False)),
                ('password_hash', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ToppingType',
            fields=[
                ('name', models.CharField(max_length=128,
                 primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('unit_cost', models.PositiveIntegerField()),
                ('image_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OwnerToken',
            fields=[
                ('token', models.CharField(max_length=128,
                 primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.owner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderToken',
            fields=[
                ('token', models.CharField(max_length=128,
                 primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='api.orderstatus'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1024)),
                ('email', models.CharField(max_length=128)),
                ('handled', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('handled_by', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.PROTECT, to='api.manager')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerToken',
            fields=[
                ('token', models.CharField(max_length=128,
                 primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.manager')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('revenue', models.PositiveIntegerField(default=0)),
                ('last_use', models.DateTimeField(
                    default=api.models.Drone.last_use_default, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('drone_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.dronetype')),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.owner')),
                ('status', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.dronestatus')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('drone', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.drone')),
                ('order', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.order')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerToken',
            fields=[
                ('token', models.CharField(max_length=128,
                 primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cone',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cone_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.conetype')),
                ('delivery', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.delivery')),
                ('ice_cream_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.icecreamtype')),
                ('topping_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='api.toppingtype')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT, to='api.customer'),
        ),
    ]
