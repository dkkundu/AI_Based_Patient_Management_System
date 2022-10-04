import logging
from django.core.cache import cache
from django.contrib.auth.models import Group

logger = logging.getLogger(__name__)


def user_has_group(user, group_name):
    if cache.get('user_groups') is None:
        cache.set('user_groups', list(
            Group.objects.values('user__id', 'user__groups__name')
        ), 200)
    user_groups = cache.get('user_groups')
    return {'user__id': user.id, 'user__groups__name': group_name
            } in user_groups