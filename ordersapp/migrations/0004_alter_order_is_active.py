from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0003_alter_order_created_alter_order_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Активный заказ'),
        ),
    ]