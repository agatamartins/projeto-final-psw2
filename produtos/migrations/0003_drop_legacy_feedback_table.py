from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_categoria_descricao_and_fornecedores'),
    ]

    operations = [
        migrations.RunSQL(
            sql='DROP TABLE IF EXISTS feedback_feedback',
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]