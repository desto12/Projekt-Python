# Generated by Django 2.0.3 on 2018-04-14 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_auto_20180414_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='updated_at',
            new_name='aktualizacja',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='available',
            new_name='dostępność',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='dopis',
            new_name='opis',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created_at',
            new_name='utworzono',
        ),
    ]