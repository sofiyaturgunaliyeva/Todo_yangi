# Generated by Django 4.2 on 2023-05-31 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiy', '0002_plan_foydalanuvchi_alter_plan_holat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='foydalanuvchi',
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=20)),
                ('yosh', models.SmallIntegerField()),
                ('kurs', models.SmallIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='talaba',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiy.talaba'),
        ),
    ]