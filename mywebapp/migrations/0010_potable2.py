# Generated by Django 4.2.7 on 2024-04-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0009_remove_issueticket_id_alter_issueticket_ticket_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='POTable2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order_no', models.CharField(max_length=100, verbose_name='Purchase order no')),
                ('purchase_order_date', models.DateField(verbose_name='Purchase order date')),
                ('po_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('link', models.FileField(blank=True, null=True, upload_to='invoice_copies/')),
            ],
        ),
    ]
