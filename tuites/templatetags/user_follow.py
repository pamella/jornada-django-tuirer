from django import template

from users.models import User

register = template.Library()

@register.simple_tag(takes_context=True)
def follow(context):
    user = context.get('user')
    profile = context.get('profile')
    user_has_followed = profile.following.filter(pk=user.pk).exists()

    if user_has_followed:
        return 'Seguindo'
    else:
        return 'Seguir'
