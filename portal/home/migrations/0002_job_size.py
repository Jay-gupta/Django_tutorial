# Generated by Django 3.0.2 on 2020-01-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_size', models.CharField(choices=[('0-$400', '30'), ('$400-$1000', '29'), ('$1000 - $3000', '28'), ('$3,000-$5,000', '27'), ('$5,000-$10,000', '26'), ('$10,000 - $25,000', '25'), ('$25,000 - $50,000', '24'), ('$25,000 - $50,000', '23')], max_length=100)),
            ],
        ),
    ]