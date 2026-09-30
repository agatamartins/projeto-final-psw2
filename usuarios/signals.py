from django.contrib.auth.models import Group, Permission
from django.db.models import Q
from django.db.models.signals import post_migrate
from django.dispatch import receiver


ROLE_PERMISSIONS = {
    'Gerente': {
        'usuarios': {'usuario': {'add', 'change', 'delete', 'view'}},
        'fornecedores': {'fornecedor': {'add', 'change', 'delete', 'view'}},
        'produtos': {
            'categoria': {'add', 'change', 'delete', 'view'},
            'produto': {'add', 'change', 'delete', 'view'},
        },
        'vendas': {
            'venda': {'add', 'change', 'delete', 'view'},
            'itemvenda': {'add', 'change', 'delete', 'view'},
        },
    },
    'Estoquista': {
        'fornecedores': {'fornecedor': {'add', 'change', 'delete', 'view'}},
        'produtos': {
            'categoria': {'add', 'change', 'delete', 'view'},
            'produto': {'add', 'change', 'delete', 'view'},
        },
        'vendas': {'venda': {'view'}},
    },
    'Vendedor': {
        'produtos': {
            'categoria': {'view'},
            'produto': {'view'},
        },
        'vendas': {
            'venda': {'add', 'view'},
            'itemvenda': {'add', 'view'},
        },
    },
}


@receiver(post_migrate)
def create_role_groups(sender, **kwargs):
    for group_name, app_permissions in ROLE_PERMISSIONS.items():
        permission_query = Q(pk__in=[])
        for app_label, models in app_permissions.items():
            for model_name, actions in models.items():
                for action in actions:
                    permission_query |= Q(
                        content_type__app_label=app_label,
                        codename=f'{action}_{model_name}',
                    )

        permissions = Permission.objects.filter(permission_query)
        group, _ = Group.objects.get_or_create(name=group_name)
        group.permissions.add(*permissions)