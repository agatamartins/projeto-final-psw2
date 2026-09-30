from decimal import Decimal, ROUND_HALF_UP

from django.db import migrations, models


def round_legacy_prices(apps, schema_editor):
    ItemVenda = apps.get_model('vendas', 'ItemVenda')
    database = schema_editor.connection.alias

    for item in ItemVenda.objects.using(database).only(
        'pk', 'preco_unitario'
    ).iterator():
        item.preco_unitario = int(
            Decimal(item.preco_unitario).quantize(
                Decimal('1'),
                rounding=ROUND_HALF_UP,
            )
        )
        item.save(using=database, update_fields=['preco_unitario'])


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            round_legacy_prices,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name='itemvenda',
            name='preco_unitario',
            field=models.IntegerField(),
        ),
    ]
