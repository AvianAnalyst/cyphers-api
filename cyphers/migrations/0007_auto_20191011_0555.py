# Generated by Django 2.2.6 on 2019-10-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyphers', '0006_auto_20191010_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cypher',
            name='dice_type',
            field=models.CharField(choices=[('d1', 'd4'), ('d2', 'd6'), ('d3', 'd8'), ('d4', 'd10'), ('d5', 'd12')], max_length=2),
        ),
    ]
