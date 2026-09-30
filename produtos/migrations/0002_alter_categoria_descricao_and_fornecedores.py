from django.db import migrations, models


def copy_supplier_links_forward(apps, schema_editor):
    Produto = apps.get_model('produtos', 'Produto')
    through = Produto.fornecedores.through
    database = schema_editor.connection.alias

    for produto in Produto.objects.using(database).exclude(
        fornecedor_id__isnull=True
    ).iterator():
        through.objects.using(database).get_or_create(
            produto_id=produto.pk,
            fornecedor_id=produto.fornecedor_id,
        )


def copy_supplier_links_backward(apps, schema_editor):
    Produto = apps.get_model('produtos', 'Produto')
    through = Produto.fornecedores.through
    database = schema_editor.connection.alias

    for produto in Produto.objects.using(database).iterator():
        fornecedor_id = through.objects.using(database).filter(
            produto_id=produto.pk
        ).order_by('fornecedor_id').values_list(
            'fornecedor_id', flat=True
        ).first()
        if fornecedor_id is not None:
            produto.fornecedor_id = fornecedor_id
            produto.save(using=database, update_fields=['fornecedor'])


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fornecedores',
            field=models.ManyToManyField(
                blank=True,
                related_name='produtos',
                to='fornecedores.fornecedor',
            ),
        ),
        migrations.RunPython(
            copy_supplier_links_forward,
            copy_supplier_links_backward,
        ),
        migrations.RemoveField(
            model_name='produto',
            name='fornecedor',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
            ),
        ),
    ]
