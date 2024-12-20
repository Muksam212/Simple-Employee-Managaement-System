# Generated by Django 4.2.17 on 2024-12-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('doj', models.DateField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('post', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('leave_count', models.IntegerField(blank=True, default=0, null=True)),
                ('on_leave', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]