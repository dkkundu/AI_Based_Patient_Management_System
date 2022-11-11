import logging
logger = logging.getLogger(__name__)


def user_has_group(user, group_name):
    if user.groups.filter(name=group_name).exists():
        return True
    else:
        return False