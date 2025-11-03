from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_address_id_alter_coupon_id_alter_item_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sales_count',
            field=models.IntegerField(default=0),
        ),
    ]