# Generated by Django 4.0 on 2021-12-19 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_user_activation_key_user_activation_key_expires'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=2, verbose_name='Пол')),
                ('language', models.TextField(blank=True, default='RU', verbose_name='Язык')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authapp.user')),
            ],
        ),
    ]