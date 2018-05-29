# Generated by Django 2.0.3 on 2018-05-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-utworzono',), 'verbose_name': 'zamówienie', 'verbose_name_plural': 'zamówienia'},
        ),
        migrations.AlterField(
            model_name='order',
            name='adres',
            field=models.CharField(max_length=30, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=30, verbose_name='Miasto'),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(max_length=30, verbose_name='Kod pocztwoy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay',
            field=models.BooleanField(default=False, verbose_name='Stan Płatności'),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(max_length=30, verbose_name='Nazwisko'),
        ),
    ]