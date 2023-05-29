# Generated by Django 4.2 on 2023-05-27 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='foydalanuvchi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plan',
            name='holat',
            field=models.CharField(choices=[('Yangi', 'Yangi'), ('Bajarilyapti', 'Bajarilyapti'), ('Bajarildi', 'Bajarildi')], max_length=20),
        ),
        migrations.AlterField(
            model_name='plan',
            name='sarlavha',
            field=models.CharField(max_length=150),
        ),
    ]
